import requests

url = "https://jsonplaceholder.typicode.com/posts"
headers = {"Content-Type": "application/json"}
data = {
    "title": "Learn Python",
    "body": "Working with Requests Library",
    "userId": 1
}

# Sending a POST request
response = requests.post(url, headers=headers, json=data)

if response.status_code == 201:  # 201 is the status for successful creation
    print("Data posted successfully:", response.json())
else:
    print("Failed to post data:", response.status_code)
