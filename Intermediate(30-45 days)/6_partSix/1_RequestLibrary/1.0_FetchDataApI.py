import requests

# Fetch data from a sample JSON placeholder API
response = requests.get("https://jsonplaceholder.typicode.com/posts")

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    print("Fetched Data:", data[:2])  # Display first two posts
else:
    print("Failed to fetch data:", response.status_code)
