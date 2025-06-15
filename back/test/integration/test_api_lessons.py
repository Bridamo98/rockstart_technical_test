import pytest


@pytest.mark.integration
def test_crud_lesson_flow(client, snapshot):
    # Prepare instructor and course
    inst_id = client.post(
        "/instructors/",
        json={"name": "Carol", "email": "carol@example.com", "bio": "Bio"},
    ).json()["id"]

    course_id = client.post(
        "/courses/",
        json={
            "title": "Course",
            "course_desc": "CD",
            "instructor_id": inst_id,
        },
    ).json()["id"]

    # Create lesson
    lesson_payload = {
        "title": "Lesson 1",
        "video_url": "https://www.youtube.com/watch?v=dQw4w9WgXcQ",
    }
    resp = client.post(f"/courses/{course_id}/lessons/", json=lesson_payload)
    assert resp.status_code == 200
    lesson = resp.json()
    snapshot.assert_match(lesson, "api_create_lesson")
    lesson_id = lesson["id"]

    # List
    resp = client.get(f"/courses/{course_id}/lessons/")
    assert resp.status_code == 200
    snapshot.assert_match(resp.json(), "api_list_lessons")

    # Update
    resp = client.put(
        f"/courses/{course_id}/lessons/{lesson_id}",
        json={"title": "Lesson 1 updated"},
    )
    assert resp.status_code == 200
    snapshot.assert_match(resp.json(), "api_update_lesson")

    # Delete
    assert client.delete(f"/courses/{course_id}/lessons/{lesson_id}").status_code == 200
    assert client.get(f"/courses/{course_id}/lessons/{lesson_id}").status_code == 404

    # Clean
    client.delete(f"/courses/{course_id}")
    client.delete(f"/instructors/{inst_id}")


@pytest.mark.integration
def test_lesson_validation_error(client):
    # Prepare instructors and courses
    inst_id = client.post(
        "/instructors/", json={"name": "Dan", "email": "dan@example.com", "bio": "B"}
    ).json()["id"]
    course_id = client.post(
        "/courses/",
        json={"title": "c", "course_desc": "d", "instructor_id": inst_id},
    ).json()["id"]

    bad_payload = {"title": "Bad", "video_url": "https://vimeo.com/12345"}
    resp = client.post(f"/courses/{course_id}/lessons/", json=bad_payload)
    assert resp.status_code == 422

    # Clean
    client.delete(f"/courses/{course_id}")
    client.delete(f"/instructors/{inst_id}")


@pytest.mark.integration
def test_lesson_not_found_for_other_course(client):
    # Prepare instructors, courses and lessons
    inst_id = client.post(
        "/instructors/", json={"name": "Eve", "email": "eve@example.com", "bio": "B"}
    ).json()["id"]
    course1_id = client.post(
        "/courses/",
        json={"title": "C1", "course_desc": "d", "instructor_id": inst_id},
    ).json()["id"]
    course2_id = client.post(
        "/courses/",
        json={"title": "C2", "course_desc": "d", "instructor_id": inst_id},
    ).json()["id"]

    lesson_id = client.post(
        f"/courses/{course1_id}/lessons/",
        json={"title": "L", "video_url": "https://youtu.be/dQw4w9WgXcQ"},
    ).json()["id"]

    for method in ("get", "put", "delete"):
        resp = getattr(client, method)(
            f"/courses/{course2_id}/lessons/{lesson_id}",
            **({"json": {"title": "x"}} if method == "put" else {}),
        )
        assert resp.status_code == 404

    # Clean
    client.delete(f"/courses/{course1_id}")
    client.delete(f"/courses/{course2_id}")
    client.delete(f"/instructors/{inst_id}")
