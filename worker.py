from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import json
import urllib.request

#read
with open("tasks.json", "r") as file:
    tasks = json.load(file) #tasks is a list containing dictionaries

#completing the work

for task in tasks:
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
            

with open("tasks.json", "w") as f:
    json.dump(tasks, f, indent=4)


