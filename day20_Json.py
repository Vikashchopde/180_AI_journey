
import json

user = {
    "name": "vikas chopde",
    "age": 23,
    "role": "Ai Engineer",
    "skills": ["python", "java", "javascript"]
}

with open("user.json", "w") as file:
       json.dump(user, file)

with open("user.json", "r") as file:
    data = json.load(file)
    print(data)
    print(data["name"])
    print(data["skills"])