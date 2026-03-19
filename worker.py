import json
import urllib.request

#read
with open("tasks.json", "r") as file:
    tasks = json.load(file) #tasks is a list containing dictionaries

#completing the work
for task in tasks:
    if task["status"] == "pending":
        with urllib.request.urlopen(task["url"]) as response:
            server_type = response.headers.get("Server", "Unknown")
            task["result"] = f"Server type: {server_type}"
        task["status"] = "complete"
        

with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)


