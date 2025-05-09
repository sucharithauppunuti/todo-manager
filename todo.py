import json
import os

TODO_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def show_tasks(tasks):
    for i, task in enumerate(tasks):
        status = "✅" if task['done'] else "❌"
        print(f"{i+1}. {task['task']} [{status}]")

def main():
    tasks = load_tasks()
    while True:
        print("\n1. Add Task\n2. Show Tasks\n3. Mark Complete\n4. Delete Task\n5. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            t = input("Enter task: ")
            tasks.append({"task": t, "done": False})
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            show_tasks(tasks)
            i = int(input("Task number to mark complete: ")) - 1
            if 0 <= i < len(tasks):
                tasks[i]["done"] = True
        elif choice == "4":
            show_tasks(tasks)
            i = int(input("Task number to delete: ")) - 1
            if 0 <= i < len(tasks):
                tasks.pop(i)
        elif choice == "5":
            save_tasks(tasks)
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
