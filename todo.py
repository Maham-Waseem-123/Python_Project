import tkinter as tk
from tkinter import messagebox

# Step 2: Create tasklist and add function
tasks = []

def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task")

# Step 3: Update the listbox
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        listbox.insert(tk.END, task)

# Step 4: Delete a Task
def delete_task():
    try:
        selected = listbox.curselection()[0]
        del tasks[selected]
        update_listbox()
    except:
        messagebox.showwarning("Input Error", "Please select a task to delete")

# Step 5: Designing the GUI
root = tk.Tk()
root.title("To-Do List")
root.geometry("300x400")

task_entry = tk.Entry(root, font="Arial 14")
task_entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack(pady=5)

listbox = tk.Listbox(root, font="Arial 12")
listbox.pack(pady=10, fill=tk.BOTH, expand=True)

del_btn = tk.Button(root, text="Delete Task", command=delete_task)
del_btn.pack(pady=5)

root.mainloop()
