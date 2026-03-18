import json

#Read
with open("tasks.json", "r") as file:
    tasks = json.load(file) #tasks is a list containing dictionaries

#Find
for task in tasks:
    if task["status"] == "pending":
        print(task["url"]) #simulate work
        task["status"] = "complete"
        

with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)


#debug purposes
print(tasks)