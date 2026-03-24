import time
import json
import fcntl
import sys
#open file to read and assign to tasks
while True:
    with open("tasks.json", "r") as file:
        fcntl.flock(file, fcntl.LOCK_SH)

        try:
            tasks = json.load(file)

            pending = 0
            complete = 0
            failed = 0

            #loop through tasks and check status
            for task in tasks:
                if task["status"] == "pending":
                    pending += 1
                elif task["status"] == "complete":
                    complete += 1
                elif task["status"] == "failed":
                    failed += 1

            print(
                f"--- Web-Scout Monitor ---\n"
                f"Pending: {pending}\n"
                f"Completed: {complete}\n"
                f"Failed: {failed}\n"
                f"--- CTRL + C to quit ----\n\n"
                f"    🔁 refreshing 🔁\n"
            )
            #print(f"Current tasks - Pending: {pending} | Complete: {complete} | Failed: {failed}\n 'CTRL + C to quit program")
            
        finally:
            fcntl.flock(file, fcntl.LOCK_UN)


    time.sleep(5)