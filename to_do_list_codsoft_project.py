import tkinter as tk
from tkinter import messagebox

# List to store tasks
tasks = []

# Function to add a task to the list
def add_task():
    task = task_entry.get()
    if task:
        tasks.append(task)
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to update the task listbox
def update_task_list():
    task_listbox.delete(0, tk.END)
    for i, task in enumerate(tasks, 1):
        task_listbox.insert(tk.END, f"{i}. {task}")

# Function to remove a selected task from the list
def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        tasks.pop(selected_task_index)
        update_task_list()
    except IndexError:
        messagebox.showwarning("Warning", "You must select a task to remove.")

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and place the widgets
task_entry = tk.Entry(root, width=50)
task_entry.pack(pady=10)

add_task_button = tk.Button(root, text="Add Task", command=add_task)
add_task_button.pack(pady=5)

task_listbox = tk.Listbox(root, width=50, height=10)
task_listbox.pack(pady=10)

remove_task_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_task_button.pack(pady=5)

# Start the main event loop
root.mainloop()