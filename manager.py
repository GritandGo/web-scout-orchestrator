import json


task = {
    "id": 1,
    "url": "https://boot.dev",
    "status": "pending"
}


tasks_list = [task]


with open("tasks.json", "w") as f:
    json.dump(tasks_list, f, indent=4)

print("Task saved to tasks.json!")
