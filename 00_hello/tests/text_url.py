import requests

r = requests.get('http://127.0.0.1:8000/hi/muazam')


def test_text_url():
    assert r.status_code ==200