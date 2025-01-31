# todo_list.py

# To-Do List class to manage tasks
class ToDoList:
    def __init__(self):
        self.tasks = []
    
    # Add a new task
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    
    # View all tasks
    def view_tasks(self):
        if not self.tasks:
            print("No tasks to display.")
        else:
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")
    
    # Mark a task as completed
    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task number.")
    
    # Delete a task
    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):
            deleted_task = self.tasks.pop(task_index - 1)
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")

# Main function to interact with the To-Do List
def main():
    todo_list = ToDoList()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter the task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_index)
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_index)
        elif choice == "5":
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

