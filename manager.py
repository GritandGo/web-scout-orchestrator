import json

with open("tasks.json", "r") as file:
    tasks = json.load(file)

new_task = {
    "id": len(tasks) + 1,
    "url": "https://google.com",
    "status": "pending",
    "result": None
}

tasks.append(new_task)

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

print("Task saved to tasks.json!")

