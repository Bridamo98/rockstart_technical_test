import pytest


@pytest.mark.integration
def test_crud_course_flow(client, snapshot):
    # Create instructor
    inst_payload = {"name": "Bob", "email": "bob@example.com", "bio": "Bio"}
    inst_id = client.post("/instructors/", json=inst_payload).json()["id"]

    # Create course
    course_payload = {
        "title": "Intro to Testing",
        "course_desc": "Course description",
        "instructor_id": inst_id,
    }
    resp = client.post("/courses/", json=course_payload)
    assert resp.status_code == 200
    course = resp.json()
    snapshot.assert_match(course, "api_create_course")
    course_id = course["id"]

    # List
    resp = client.get("/courses/")
    assert resp.status_code == 200
    snapshot.assert_match(resp.json(), "api_list_courses")

    # Get by id
    assert client.get(f"/courses/{course_id}").status_code == 200

    # Update
    update_payload = {"title": "Intro to Testing – updated"}
    resp = client.put(f"/courses/{course_id}", json=update_payload)
    assert resp.status_code == 200
    snapshot.assert_match(resp.json(), "api_update_course")

    # Delete
    assert client.delete(f"/courses/{course_id}").status_code == 200
    assert client.get(f"/courses/{course_id}").status_code == 404

    # Clean
    client.delete(f"/instructors/{inst_id}")
