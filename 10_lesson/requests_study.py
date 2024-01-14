import requests
import json

windows_activate = ".\venv\Scripts\activate"
linux_macos_activate = "source venv/bin/activate"


site = "https://jsonplaceholder.typicode.com/posts/1"
response_get = requests.get(url=site)

for header, value in response_get.headers.items():
    print(f"Header: {header} --> Value: {value}")
                                         
print(response_get.text)
print("------------")

body = {
    "userId": 12,
    "title": "test",
    "body": "test"
}
headers = {
    'Content-Type': 'application/json; charset=utf-8'
}

response_post = requests.post(url=site, json=body, headers=headers)
print(response_post.status_code)
print(response_post.reason)
print(response_post.text)
print("------------")

data = {
    "title": "test_put"
}
response_put = requests.put(url=site, data=data)

print(response_put.status_code)
print(response_put.reason)
print(response_put.text)

print("------------")

response_patch = requests.patch(url=site, data=data)
print(response_patch.status_code)
print(response_patch.reason)
print(response_patch.text)

print("------------")

response_delete = requests.delete(url=site)
print(response_delete.status_code)
print(response_delete.reason)
print(response_delete.text)

