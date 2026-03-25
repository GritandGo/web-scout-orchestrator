import json
import sys
import fcntl

#user input and validation
def user_input():
    while True:
        user_url = input("Enter a URL for the Scout to investigate, or enter 'exit' to quit program: ").strip()
        url_lower = user_url.lower()

        if not (url_lower.startswith(("https://", "http://")) or url_lower == "exit"):
            print("URL must start with https://, http://, or type 'exit'")
            continue
        if url_lower == "exit":
            sys.exit(0)
        return user_url
    
#create new task/file locking
def add_task(url):
    with open("tasks.json", "r+") as file:
        fcntl.flock(file, fcntl.LOCK_EX)
        
        try:
            tasks = json.load(file)

            new_id = max((task["id"] for task in tasks), default=0) + 1

            new_task = {
                "id": new_id,
                "url": url,
                "status": "pending",
                "result": None
            }

            tasks.append(new_task)
            file.seek(0) #move pointer to start of file
            json.dump(tasks, file, indent=4)
            file.truncate()
        finally:
            fcntl.flock(file, fcntl.LOCK_UN)


def main():
    while True:
        url = user_input()
        try:
            add_task(url)
            print(f"Task for {url} saved successfully.")
        except Exception as e:
            print(f"Failed to save task. {e}")

if __name__ == "__main__":
    main()
