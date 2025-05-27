import os

# Task Manager class to handle all task-related operations
class TodoListManager:
    def __init__(self):
        self.tasks = []
        self.load_tasks()

    def load_tasks(self):
        """Load tasks from the tasks.txt file."""
        if os.path.exists("tasks.txt"):
            with open("tasks.txt", "r") as file:
                self.tasks = file.readlines()

    def save_tasks(self):
        """Save tasks to the tasks.txt file."""
        with open("tasks.txt", "w") as file:
            for task in self.tasks:
                file.write(task)

    def add_task(self, task):
        """Add a new task to the list."""
        self.tasks.append(task + "\n")
        self.save_tasks()
        print(f"Task '{task}' added.")

    def remove_task(self, task_index):
        """Remove a task by index."""
        try:
            task = self.tasks.pop(task_index)
            self.save_tasks()
            print(f"Task '{task.strip()}' removed.")
        except IndexError:
            print("Invalid task number. Please try again.")

    def view_tasks(self):
        """Display all tasks."""
        if not self.tasks:
            print("No tasks to display.")
        else:
            for idx, task in enumerate(self.tasks, start=1):
                print(f"{idx}. {task.strip()}")

    def menu(self):
        """Display the menu and get user input."""
        while True:
            print("\nTo-Do List Manager")
            print("1. View Tasks")
            print("2. Add Task")
            print("3. Remove Task")
            print("4. Exit")

            choice = input("Choose an option (1/2/3/4): ")

            if choice == "1":
                self.view_tasks()
            elif choice == "2":
                task = input("Enter a new task: ")
                self.add_task(task)
            elif choice == "3":
                self.view_tasks()
                try:
                    task_index = int(input("Enter task number to remove: ")) - 1
                    self.remove_task(task_index)
                except ValueError:
                    print("Please enter a valid task number.")
            elif choice == "4":
                print("Exiting To-Do List Manager.")
                break
            else:
                print("Invalid choice. Please try again.")

# Create an instance of TodoListManager and run the menu
if __name__ == "__main__":
    todo_manager = TodoListManager()
    todo_manager.menu()
