import pytest
import requests

@pytest.mark.smoke
def test_get_all_users(url , api_session):
    response = api_session.get(f"{url}/users" ,timeout=6 )
    data = response.json()
    assert response.status_code ==200 , "status code is not 200 "
    assert isinstance(data , list)
    assert len(data)==10 ," not 10 users !"


def test_get_single_user(url , api_session):
    response = api_session.get(f"{url}/users/1"  ,timeout=6)
    data = response.json()
    assert response.status_code ==200 , "status code is not 200 "
    assert data["id"] ==1 , " id is not 1 "
    assert  isinstance(data["name"], str)


def test_create_user(url , api_session):
    body={
        "name" : "abc",
        "email" : "abc@gmail.com",
        "username" : "xyz"
    }
    response = api_session.post(f"{url}/users" , timeout=6 , json=body)
    data = response.json()
    assert response.status_code==201 , "status code is not 201 "
    assert data["name"]=="abc", "name doesnt match "


@pytest.mark.parametrize("id" , [1,2,3])
def test_get_some_users(url , api_session , id):
    response = api_session.get(f"{url}/users/{id}" ,timeout=6)
    data = response.json()
    assert response.status_code==200 , f"status code is not 200 for id {id}"
    assert "name" in data , "name feild is missing"


