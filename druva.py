class Task:
    def _init_(self, description, due_date, priority):
        self.description = description
        self.due_date = due_date
        self.priority = priority
        self.completed = False

    def _str_(self):
        return f"{self.description} (Due Date: {self.due_date}, Priority: {self.priority})"


class TaskList:
    def _init_(self):
        self.tasks = []
        self.completed_tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def mark_as_completed(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
            self.completed_tasks.append(task)
            task.completed = True

    def update_task(self, task, updated_description, updated_due_date, updated_priority):
        task.description = updated_description
        task.due_date = updated_due_date
        task.priority = updated_priority

    def remove_task(self, task):
        if task in self.tasks:
            self.tasks.remove(task)
        elif task in self.completed_tasks:
            self.completed_tasks.remove(task)

    def display_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            print(f"- {task}")

        print("\nCompleted Tasks:")
        for task in self.completed_tasks:
            print(f"- {task}")


# User Input
task_description = input("Enter task description: ")
task_due_date = input("Enter due date (dd/mm/yyyy): ")
task_priority = input("Enter priority (1- High, 2- Medium, 3- Low): ")

# Create Task
task = Task(task_description, task_due_date, task_priority)

# Initialize Task List
task_list = TaskList()

# Add Task
task_list.add_task(task)

# Display Tasks
task_list.display_tasks()