import json

path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/6_daySix/data.json"

with open(path, "r") as file:
    data = json.load(file)
    print(data)