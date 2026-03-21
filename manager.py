import json
import sys

with open("tasks.json", "r") as file:
    tasks = json.load(file)


while True:
    user_url = input("Enter a URL for the Scout to investigate, or enter 'exit' to quit program: ").strip()
    url_lower = user_url.lower()
    if not (url_lower.startswith(("https://", "http://")) or url_lower == "exit"):
        print("URL must start with https://, http://, or 'exit' (case sensitive)")
        continue

    if url_lower == "exit":
        sys.exit(0)

    new_task = {
        "id": len(tasks) + 1,
        "url": user_url,
        "status": "pending",
        "result": None
    }

    tasks.append(new_task)
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)

