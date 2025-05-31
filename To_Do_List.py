class Task:
    def __init__(self, description, done=False):
        self.description = description
        self.done = done

    def __str__(self):
        status = "[x]" if self.done else "[ ]"
        return f"{status} {self.description}"

def load_tasks(filename):
    tasks = []
    try:
        with open(filename, 'r') as file:
            for line in file:
                parts = line.strip().split('|')
                description = parts[0]
                done = parts[1] == 'True'
                tasks.append(Task(description, done))
    except FileNotFoundError:
        pass
    return tasks

def save_tasks(filename, tasks):
    with open(filename, 'w') as file:
        for task in tasks:
            file.write(f"{task.description}|{task.done}\n")

def display_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def main():
    filename = "tasks.txt"
    tasks = load_tasks(filename)

    while True:
        print("\nMenu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Mark task as done")
        print("4. Edit task")
        print("5. Remove task")
        print("6. Save and Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            desc = input("Enter new task description: ")
            tasks.append(Task(desc))
            print("Task added.")
        elif choice == '3':
            display_tasks(tasks)
            try:
                num = int(input("Task number to mark done: "))
                if 1 <= num <= len(tasks):
                    tasks[num - 1].done = True
                    print("Task marked as done.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '4':
            display_tasks(tasks)
            try:
                num = int(input("Task number to edit: "))
                if 1 <= num <= len(tasks):
                    new_desc = input("Enter new description: ")
                    tasks[num - 1].description = new_desc
                    print("Task updated.")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '5':
            display_tasks(tasks)
            try:
                num = int(input("Task number to remove: "))
                if 1 <= num <= len(tasks):
                    removed = tasks.pop(num - 1)
                    print(f"Removed: {removed.description}")
                else:
                    print("Invalid number.")
            except ValueError:
                print("Please enter a valid number.")
        elif choice == '6':
            save_tasks(filename, tasks)
            print("Tasks saved. Goodbye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
