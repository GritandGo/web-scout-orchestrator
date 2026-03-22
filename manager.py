import json
import sys
import fcntl


while True:
    user_url = input("Enter a URL for the Scout to investigate, or enter 'exit' to quit program: ").strip()
    url_lower = user_url.lower()

    if not (url_lower.startswith(("https://", "http://")) or url_lower == "exit"):
        print("URL must start with https://, http://, or 'exit' (case sensitive)")
        continue
    if url_lower == "exit":
        sys.exit(0)

    #open file and lock it
    with open("tasks.json", "r+") as file:
        fcntl.flock(file, fcntl.LOCK_EX)

        try:
            tasks = json.load(file)

            new_id = max((task["id"] for task in tasks), default=0) + 1

            new_task = {
                "id": new_id,
                "url": user_url,
                "status": "pending",
                "result": None
            }

            tasks.append(new_task)
            file.seek(0) #move pointer to start of file
            json.dump(tasks, file, indent=4)
            file.truncate()
        finally:
            fcntl.flock(file, fcntl.LOCK_UN)

