import json

with open("tasks.json", "r") as file:
    tasks = json.load(file)


user_url = input("Enter a URL for the Scout to investigate: ").strip()
if not (user_url.startswith("https://") or user_url.startswith("http://")):
    raise ValueError("URL must start with https:// or http://")

new_task = {
    "id": len(tasks) + 1,
    "url": user_url,
    "status": "pending",
    "result": None
}

tasks.append(new_task)

with open("tasks.json", "w") as file:
    json.dump(tasks, file, indent=4)

print("Task saved to tasks.json!")

