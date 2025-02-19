# Initialize the task list
tasks = []

def add_task(task):
    """Add a task to the to-do list."""
    tasks.append({'task': task, 'completed': False})
    print(f"Task added: {task}")

def mark_completed(task_number):
    """Mark a task as completed by its number."""
    if 0 <= task_number < len(tasks):
        tasks[task_number]['completed'] = True
        print(f"Task marked as completed: {tasks[task_number]['task']}")
    else:
        print("Invalid task number.")

def display_tasks():
    """Display all tasks with their status."""
    if not tasks:
        print("No tasks in the to-do list.")
        return
    
    print("\nTo-Do List:")
    for i, task in enumerate(tasks):
        status = "✔️" if task['completed'] else "❌"
        print(f"{i}. {task['task']} [{status}]")

def delete_task(task_number):
    """Delete a task by its number."""
    if 0 <= task_number < len(tasks):
        removed_task = tasks.pop(task_number)
        print(f"Task deleted: {removed_task['task']}")
    else:
        print("Invalid task number.")
