import json
import os
import sys
import time

TASKS_FILE = "tasks_data.json"

def load_tasks():
    if os.path.exists(TASKS_FILE):
        try:
            with open(TASKS_FILE, "r") as f:
                return json.load(f)
        except Exception:
            return []
    return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

def clear_screen():
    os.system("clear" if os.name != "nt" else "cls")

def print_banner():
    print("\033[1;36m====================================\033[0m")
    print("\033[1;32m       CLI TASK MANAGER PRO         \033[0m")
    print("\033[1;36m====================================\033[0m")

def show_progress():
    print("\n\033[1;33mProcessing request...\033[0m")
    for i in range(1, 21):
        time.sleep(0.03)
        sys.stdout.write(f"\r[\033[1;32m{'#' * i}{'.' * (20 - i)}\033[0m] {i * 5}%")
        sys.stdout.flush()
    print("\n")

def list_tasks(tasks):
    if not tasks:
        print("\033[1;31mNo tasks available.\033[0m")
        return
    print("\n\033[1;35mYour Current Tasks:\033[0m")
    for idx, task in enumerate(tasks, 1):
        status = "\033[1;32m[DONE]\033[0m" if task.get("done") else "\033[1;33m[PENDING]\033[0m"
        print(f"{idx}. {task['title']} {status}")

def main():
    tasks = load_tasks()
    while True:
        clear_screen()
        print_banner()
        list_tasks(tasks)
        print("\n\033[1;34mMenu Options:\033[0m")
        print("1. Add Task")
        print("2. Mark Task as Done")
        print("3. Delete Task")
        print("4. Exit")
        
        choice = input("\n\033[1;37mSelect an option (1-4): \033[0m").strip()
        
        if choice == "1":
            title = input("Enter task title: ").strip()
            if title:
                tasks.append({"title": title, "done": False})
                show_progress()
                save_tasks(tasks)
        elif choice == "2":
            if tasks:
                try:
                    num = int(input("Enter task number to mark done: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["done"] = True
                        show_progress()
                        save_tasks(tasks)
                except ValueError:
                    pass
        elif choice == "3":
            if tasks:
                try:
                    num = int(input("Enter task number to delete: "))
                    if 1 <= num <= len(tasks):
                        tasks.pop(num - 1)
                        show_progress()
                        save_tasks(tasks)
                except ValueError:
                    pass
        elif choice == "4":
            print("\033[1;32mExiting... Goodbye!\033[0m")
            break

if __name__ == "__main__":
    main()

