import pytest
import os
from dotenv import load_dotenv
load_dotenv()
import requests

base_url = os.getenv("BASE_URL")


@pytest.fixture
def url():
    return base_url

@pytest.fixture(scope="module")
def api_session():
    with requests.Session() as session:
        session.headers.update({
            "Content-Type" : "application/json"
        })
        yield session



