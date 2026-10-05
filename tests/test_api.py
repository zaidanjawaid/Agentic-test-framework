import requests

BASE = "https://jsonplaceholder.typicode.com"


def test_get_post():
    r = requests.get(f"{BASE}/posts/1", timeout=10)
    assert r.status_code == 200
    assert r.json()["id"] == 1


def test_create_post():
    r = requests.post(f"{BASE}/posts", json={"title": "QA", "body": "hi", "userId": 1}, timeout=10)
    assert r.status_code == 201
    assert r.json()["title"] == "QA"
