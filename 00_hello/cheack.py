import requests

r = requests.get('http://127.0.0.1:8000/hi')

print(r.text)

print(r.status_code)

print(r.headers)

print(r.url)

print(r.content)
