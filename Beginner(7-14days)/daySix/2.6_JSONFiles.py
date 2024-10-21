import json
 
path = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/daySix/data.json"

data = {
    "name": "Python",
    "age": 30,
    "city": "Moshi"
}

with open(path, "w") as file:
    json.dump(data, file)

print(f"File saved on {path}")