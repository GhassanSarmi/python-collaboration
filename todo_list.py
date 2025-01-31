# todo_list.py

# To-Do List class to manage tasks
class ToDoList:
    def __init__(self):
        self.tasks = []  # Initialize an empty list to store tasks
    
    # Add a new task
    def add_task(self, task):
        self.tasks.append({"task": task, "completed": False})
    
    # View all tasks
    def view_tasks(self):
        if not self.tasks:  # Check if there are no tasks
            print("No tasks to display.")
        else:
            # Print each task with its status (Completed or Pending)
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")
    
    # Mark a task as completed
    def mark_completed(self, task_index):
        if 0 < task_index <= len(self.tasks):  # Ensure the task index is valid
            self.tasks[task_index - 1]["completed"] = True
            print(f"Task {task_index} marked as completed.")
        else:
            print("Invalid task number.")
    
    # Delete a task
    def delete_task(self, task_index):
        if 0 < task_index <= len(self.tasks):  # Ensure the task index is valid
            deleted_task = self.tasks.pop(task_index - 1)  # Remove the task from the list
            print(f"Task '{deleted_task['task']}' deleted.")
        else:
            print("Invalid task number.")

# Main function to interact with the To-Do List
def main():
    todo_list = ToDoList()  # Create an instance of the ToDoList class
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Mark task as completed")
        print("4. Delete task")
        print("5. Exit")
        
        choice = input("Enter your choice: ")  # Get the user's choice from the menu

        if choice == "1":
            task = input("Enter the task: ")  # Get the task description
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.view_tasks()  # Display all tasks
        elif choice == "3":
            task_index = int(input("Enter the task number to mark as completed: "))
            todo_list.mark_completed(task_index)  # Mark the selected task as completed
        elif choice == "4":
            task_index = int(input("Enter the task number to delete: "))
            todo_list.delete_task(task_index)  # Delete the selected task
        elif choice == "5":
            print("Exiting program.")  # Exit the program
            break
        else:
            print("Invalid choice. Please try again.")  # If the user enters an invalid option

if __name__ == "__main__":
    main()  # Run the main function when the script is executed
