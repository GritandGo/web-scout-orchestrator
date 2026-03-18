import json


tasks_list = [
    {
    "id": 1,
    "url": "https://boot.dev",
    "status": "pending"
    },
    {
    "id": 2,
    "url": "https://boot.dev",
    "status": "pending"
    }
]


with open("tasks.json", "w") as file:
    json.dump(tasks_list, file, indent=4)

print("Task saved to tasks.json!")
print(tasks_list) #debug purposes
