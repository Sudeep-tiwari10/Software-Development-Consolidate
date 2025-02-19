#first we have install tkinter to import necessary libraries.
import tkinter as tk
from tkinter import messagebox

def add_task():
    """Add a new task to the list."""
    task = entry.get()  # Get the task text from the entry widget
    if task != "":
        listbox.insert(tk.END, task)  # Add the task to the listbox
        entry.delete(0, tk.END)  # Clear the input field
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def remove_task():
    """Remove the selected task from the list."""
    try:
        task_index = listbox.curselection()[0]  # Get the index of selected task
        listbox.delete(task_index)  # Delete the task
    except IndexError:
        messagebox.showwarning("Selection Error", "Please select a task to remove.")

def clear_tasks():
    """Clear all tasks from the list."""
    listbox.delete(0, tk.END)  # Delete all tasks in the listbox

# Create the main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# Create a Label for the title
label = tk.Label(root, text="To-Do List", font=("Helvetica", 16))
label.pack(pady=10)

# Create an Entry widget for task input
entry = tk.Entry(root, width=35)
entry.pack(pady=10)

# Create a Listbox to display tasks
listbox = tk.Listbox(root, width=40, height=10)
listbox.pack(pady=10)

# Create buttons for Add, Remove, and Clear tasks
button_add = tk.Button(root, text="Add Task", width=15, command=add_task)
button_add.pack(pady=5)

button_remove = tk.Button(root, text="Remove Task", width=15, command=remove_task)
button_remove.pack(pady=5)

button_clear = tk.Button(root, text="Clear All", width=15, command=clear_tasks)
button_clear.pack(pady=5)

# Run the application
root.mainloop()
