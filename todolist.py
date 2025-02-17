import tkinter as tk
from tkinter import messagebox
import json
import os

# File to store tasks
TODO_FILE = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

# Add a new task
def add_task():
    task = task_entry.get().strip()
    if task:
        tasks.append({"task": task, "completed": False})
        save_tasks(tasks)
        update_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# Mark a task as completed
def mark_completed():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        tasks[index]["completed"] = True
        save_tasks(tasks)
        update_list()
    else:
        messagebox.showwarning("Warning", "Select a task to mark as completed!")

# Delete a selected task
def delete_task():
    selected = task_listbox.curselection()
    if selected:
        index = selected[0]
        del tasks[index]
        save_tasks(tasks)
        update_list()
    else:
        messagebox.showwarning("Warning", "Select a task to delete!")

# Update the task list in GUI
def update_list():
    task_listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔ " if task["completed"] else "❌ "
        task_listbox.insert(tk.END, status + task["task"])

# Initialize GUI
app = tk.Tk()
app.title("To-Do List App")
app.geometry("400x450")
app.config(bg="#f5f5f5")

# Load existing tasks
tasks = load_tasks()

# Task Entry Field
task_entry = tk.Entry(app, width=40)
task_entry.pack(pady=10)

# Buttons
add_button = tk.Button(app, text="Add Task", command=add_task, bg="#4CAF50", fg="white")
add_button.pack(pady=5)

mark_button = tk.Button(app, text="Mark Completed", command=mark_completed, bg="#FFC107", fg="black")
mark_button.pack(pady=5)

delete_button = tk.Button(app, text="Delete Task", command=delete_task, bg="#F44336", fg="white")
delete_button.pack(pady=5)

# Task Listbox
task_listbox = tk.Listbox(app, width=50, height=15)
task_listbox.pack(pady=10)

# Load tasks into listbox
update_list()

# Run the application
app.mainloop()
