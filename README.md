# web-scout-orchestrator (Technical Proof-of-Concept)

## The Goal
This project was built as a personal learning experience and my inital endeavor into learning and implementing **Backend Infrastructure** and **Distributed Systems** concepts. My goal was not to build a complex web scout or scraper, but to create a very simple proof of concept **Task Queue** that can manage asynchronous work across multiple independent processes. I hope to continue to come back to this project and refactor, improve, and implement new ideas and concepts as I learn them.

## Concepts explored or utilized:
*   **Concurrency & Thread Safety**: Implemented `fcntl.flock` (File Locking) to ensure data integrity when multiple workers or managers access the shared JSON database simultaneously.
*   **Persistent Task Queue**: Built a "Manager" to add "work" to the JSON file and a "Worker" to process it, using a JSON-based state machine (`pending` -> `completed` -> `failed`).
*   **Atomic Updates**: Used built-in Python methods `seek(0)` and `truncate()`to ensure file writes are clean and corruption-free.
*   **Network durability**: Integrated specific error handling for `HTTPError` and `URLError` to ensure the system remains stable even when remote servers are unreachable.
*   **Observability**: Created a simple real-time `monitor.py` dashboard to track the basic throughput of the system.

## Architecture
1.  **Manager (`manager.py`)**: An interactive CLI for inserting URLs into the system with very basic input sanitization.
2.  **Worker (`worker.py`)**: An always-on background service that "Polls" the queue and fingerprints remote server types.
3.  **Monitor (`monitor.py`)**: A live dashboard providing a view of system operations.

## JSON as a Database
I chose a **JSON File** as my simple database because this is a small-scale project, I wanted to practice basic data serialization, and at the time of this entry I have had no experience working with databases.

## How to Run
1. Start the Monitor: `python3 monitor.py`
2. Start the Worker: `python3 worker.py` (Open a second terminal for a second worker!)
3. Add Work: `python3 manager.py`

Thank you for taking a look and good luck out there!