# View all tasks
    def view_tasks(self):
        if not self.tasks:  # Check if there are no tasks
            print("No tasks to display.")
        else:
            # Print each task with its status (Completed or Pending)
            for i, task in enumerate(self.tasks, start=1):
                status = "Completed" if task["completed"] else "Pending"
                print(f"{i}. {task['task']} [{status}]")

put code here
