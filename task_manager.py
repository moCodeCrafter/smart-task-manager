tasks = []

def add_task():
    task = input("Enter the task: ")
    priority = 1
    lower_task = task.lower()
    if "important" in lower_task or "urgent" in lower_task:
        priority = 3
    elif "medium" in lower_task:
        priority = 2
    tasks.append({"text": task, "priority": priority})
    print("Task added.")

def show_tasks():
    if not tasks:
        print("No tasks yet.")
        return
    sorted_tasks = sorted(tasks, key=lambda x: x["priority"], reverse=True)
    for i, t in enumerate(sorted_tasks, 1):
        print(f"{i}. [Priority {t['priority']}] {t['text']}")

def delete_task():
    show_tasks()
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            to_delete = sorted(tasks, key=lambda x: x["priority"], reverse=True)[num]
            tasks.remove(to_delete)
            print("Task deleted.")
        else:
            print("Invalid number.")
    except ValueError:
        print("Please enter a valid number.")

def main():
    while True:
        print("\n1. Add task")
        print("2. Show tasks")
        print("3. Delete task")
        print("4. Exit")
        choice = input("Your choice: ")
        if choice == "1":
            add_task()
        elif choice == "2":
            show_tasks()
        elif choice == "3":
            delete_task()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()