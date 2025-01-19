import tkinter as tk
from tkinter import messagebox

def add_task(task_manager, task_name_entry, task_deadline_entry, task_priority_var):
    task_name = task_name_entry.get()
    task_deadline = task_deadline_entry.get()
    task_priority = task_priority_var.get()

    if task_name and task_deadline and task_priority:
        task_manager.add_task(task_name, task_deadline, task_priority)
        messagebox.showinfo("Success", "Task added successfully!")
    else:
        messagebox.showerror("Error", "Please fill in all fields.")

def launch_gui(task_manager, calendar, reminder_system):
    root = tk.Tk()
    root.title("Smart Task Manager")

    # Create and place GUI components
    tk.Label(root, text="Task Name").grid(row=0, column=0, padx=10, pady=5)
    tk.Label(root, text="Task Deadline (YYYY-MM-DD)").grid(row=1, column=0, padx=10, pady=5)
    tk.Label(root, text="Priority").grid(row=2, column=0, padx=10, pady=5)

    task_name_entry = tk.Entry(root, width=30)
    task_deadline_entry = tk.Entry(root, width=30)
    task_name_entry.grid(row=0, column=1, padx=10, pady=5)
    task_deadline_entry.grid(row=1, column=1, padx=10, pady=5)

    task_priority_var = tk.StringVar(value="Medium")
    tk.OptionMenu(root, task_priority_var, "High", "Medium", "Low").grid(row=2, column=1, padx=10, pady=5)

    tk.Button(
        root,
        text="Add Task",
        command=lambda: add_task(task_manager, task_name_entry, task_deadline_entry, task_priority_var)
    ).grid(row=3, column=0, columnspan=2, pady=10)

    root.mainloop()
