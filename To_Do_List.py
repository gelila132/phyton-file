"""3)	Build a to-do list manager that
•	Allows users to add tasks with priorities (e.g., "Buy milk - high").
•	Lets them view the current list, delete tasks by number, and mark tasks as complete.
•	Keeps looping until the user types "exit".
•	Shows a summary at the end: number of completed tasks vs pending."""


tasks = []
done_count = 0

while True:
    cmd = input("\n(add/view/done/del/exit): ").lower()
    
    if cmd == "exit": break
    
    if cmd == "add":
        tasks.append(f"{input('Task: ')} - {input('Priority: ')}")
    
    elif cmd == "view":
        for i, t in enumerate(tasks, 1): print(f"{i}. {t}")
            
    elif cmd in ["done", "del"]:
        idx = int(input("Task #: ")) - 1
        removed = tasks.pop(idx)
        if cmd == "done": done_count += 1
        print(f"Removed: {removed}")

print(f"\nDone: {done_count} | Pending: {len(tasks)}")