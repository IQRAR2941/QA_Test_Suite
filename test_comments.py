import pytest

@pytest.mark.parametrize("post_id", [1, 2, 3])
def test_get_comments_for_post(url, api_session, post_id):
    response = api_session.get(f"{url}/comments", params={"postId": post_id}, timeout=6)
    data = response.json()
    assert response.status_code == 200, f"Expected 200 for postId {post_id}"
    assert isinstance(data, list), f"Response should be list for postId {post_id}"
    assert len(data) > 0, f"No comments for postId {post_id}"
    for comment in data:
        assert "email" in comment, f"Missing email in comment for postId {post_id}"
 
def test_get_single_comment(url, api_session):
    response = api_session.get(f"{url}/comments/1", timeout=6)
    data = response.json()
    assert response.status_code == 200, "Expected 200"
    assert data["id"] == 1, "Wrong comment returned"
    assert "@" in data["email"], "Invalid email format"

def test_comment_email_format(url, api_session):
    response = api_session.get(f"{url}/comments", params={"postId": 1}, timeout=6)
    data = response.json()
    assert response.status_code == 200, "Expected 200"
    for comment in data:
        assert "@" in comment["email"], f"Invalid email: {comment['email']}"