import pytest

@pytest.mark.parametrize("user_id", [1, 2, 3])
def test_get_posts_by_user(url, api_session, user_id):
    response = api_session.get(f"{url}/posts", params={"userId": user_id}, timeout=6)
    data = response.json()
    assert response.status_code == 200, f"Expected 200 for userId {user_id}"
    assert isinstance(data, list), f"Response should be a list for userId {user_id}"
    assert len(data) > 0, f"No posts found for userId {user_id}"

def test_get_all_posts(url, api_session):
    response = api_session.get(f"{url}/posts", timeout=6)
    data = response.json()
    assert response.status_code == 200, "Expected 200"
    assert isinstance(data, list), "Response should be a list"
    assert len(data) == 100, "Expected exactly 100 posts"

def test_create_and_verify_post(url, api_session):
    body = {"title": "test post", "body": "test body", "userId": 1}
    response = api_session.post(f"{url}/posts", json=body, timeout=6)
    data = response.json()
    assert response.status_code == 201, "Expected 201"
    assert data["title"] == "test post", "Title mismatch"
    assert data["userId"] == 1, "userId mismatch"

def test_update_post(url, api_session):
    body = {"title": "updated title", "body": "updated body", "userId": 1}
    response = api_session.put(f"{url}/posts/1", json=body, timeout=6)
    data = response.json()
    assert response.status_code == 200, "Expected 200"
    assert data["title"] == "updated title", "Title mismatch after update"