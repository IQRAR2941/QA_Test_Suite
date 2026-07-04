import requests
import pytest 

@pytest.mark.parametrize("post_id" ,[1,3,5,7,9])
def test_get_post(post_id , url , api_session):
    response = api_session.get(f"{url}/posts/{post_id}" , timeout=6 )
    data = response.json()
    assert response.status_code == 200 , f"status code not valid for post_id {post_id}"
    assert "title" in data , f"title doesn't exist ! for post_id {post_id}"
    assert data["id"]==post_id, f"ID doesnt match for post_id {post_id}"


@pytest.mark.parametrize("title,body,userId",[
    ("first post", "first body", 1),
    ("second post", "second body", 2),
    ("third post", "third body", 3)])
def test_create_post(url , api_session , title , body ,userId):
    body = {
        "title" : f"{title}" ,
        "body" : f"{body}" ,
        "userId" : userId
    }
    respose = api_session.post(f"{url}/posts" , json=body , timeout=6)
    data = respose.json()
    assert respose.status_code==201 , f"status code not 201 for user_id {userId}"
    assert data["title"]==f"{title}" , f"title doesnt match for user_id{userId}"