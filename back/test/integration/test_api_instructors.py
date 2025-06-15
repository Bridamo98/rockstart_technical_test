import pytest


@pytest.mark.integration
def test_create_and_get_instructor(client, snapshot):
    # Create instructor
    payload = {"name": "Alice", "email": "alice@example.com", "bio": "Instructor"}
    resp = client.post("/instructors/", json=payload)
    assert resp.status_code == 200
    data = resp.json()
    snapshot.assert_match(data, "api_create_instructor")

    # List
    list_resp = client.get("/instructors/")
    assert list_resp.status_code == 200
    snapshot.assert_match(list_resp.json(), "api_list_instructors")

    # Clean
    del_id = data.get("id")
    client.delete(f"/instructors/{del_id}")
