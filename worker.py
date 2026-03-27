import time
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json
import urllib.request
import fcntl

def complete_task(task):
    if task["status"] == "pending":
        try:
            req = urllib.request.Request(
                task["url"],
                headers={"User-Agent": "Mozilla/5.0"}
            )

            with urllib.request.urlopen(req, timeout=5) as response:
                server_type = response.headers.get("Server", "Unknown")
                task["result"] = f"Server type: {server_type}"

            task["status"] = "complete"

        except HTTPError as e:
            task["status"] = "failed"
            task["result"] = f"HTTP Error: {e.code}"
            
            
        except URLError as e:
            task["status"] = "failed"
            task["result"] = f"Url Error: {e.reason}"
            
            
        except Exception as e:
            task["status"] = "failed"
            task["result"] = f"Unexpected Error: {e}" 
            
    

def main():
    while True:
        was_updated = False
        with open("tasks.json", "r+") as file:
            fcntl.flock(file, fcntl.LOCK_EX)

            try:
                tasks = json.load(file)

                for task in tasks:
                    if task["status"] == "pending":
                        complete_task(task)
                        was_updated = True
                        
                if was_updated == True:
                    file.seek(0) #move pointer to start of file
                    json.dump(tasks, file, indent=4)
                    file.truncate()
            finally:
                fcntl.flock(file, fcntl.LOCK_UN)


        time.sleep(5)


if __name__ == "__main__":
    main()