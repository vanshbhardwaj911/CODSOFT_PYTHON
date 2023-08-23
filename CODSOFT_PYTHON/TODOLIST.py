import random
import string
import tkinter as tk
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    new_task = new_task_var.get()
    if len(new_task) == 0:
        messagebox.showinfo('Input Error', 'Task field is empty.')
    else:
        task_items.append(new_task)
        cursor.execute('INSERT INTO todo_tasks VALUES (?)', (new_task,))
        update_list()
        new_task_var.set("")

def update_list():
    task_list.delete(0, 'end')
    for index, task_item in enumerate(task_items, start=1):
        task_list.insert('end', f"\u2022 {task_item}")

def delete_task():
    try:
        selected_task = task_list.get(task_list.curselection())
        if selected_task in task_items:
            task_items.remove(selected_task)
            update_list()
            cursor.execute('DELETE FROM todo_tasks WHERE task = ?', (selected_task,))
    except:
        messagebox.showinfo('Error', 'No task selected.')

def delete_all_tasks():
    confirm = messagebox.askyesno('Delete All', 'Are you sure you want to delete all tasks?')
    if confirm:
        task_items.clear()
        cursor.execute('DELETE FROM todo_tasks')
        update_list()

def close_app():
    save_tasks()
    connection.commit()
    connection.close()
    root.destroy()

def save_tasks():
    cursor.execute('DELETE FROM todo_tasks')
    for task_item in task_items:
        cursor.execute('INSERT INTO todo_tasks VALUES (?)', (task_item,))

if __name__ == "__main__":
    root = tk.Tk()
    root.title("To-Do List")
    root.geometry("500x400")
    root.configure(bg="#223366")

    connection = sql.connect('task_manager.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS todo_tasks (task TEXT)')

    task_items = []

    header_frame = tk.Frame(root, bg="#223366")
    content_frame = tk.Frame(root, bg="#223366")
    task_frame = tk.Frame(content_frame, bg="#223366")

    header_frame.pack(fill="both", pady=10)
    content_frame.pack(expand=True, fill="both")
    task_frame.pack(side="left", padx=20)

    header_label = tk.Label(header_frame, text="To-Do List", font=("Arial", 24, "bold"), bg="#223366", fg="#FF9900")
    header_label.pack(padx=20, pady=10)

    new_task_var = tk.StringVar()
    new_task_entry = tk.Entry(task_frame, textvariable=new_task_var, font=("Calibri", 14), width=20)
    new_task_entry.grid(row=0, column=0, padx=10, pady=10)

    add_button = tk.Button(task_frame, text="Note Task", font=("Arial", 12, "bold"), command=add_task, bg="#44AA44", fg="#FFFFFF")
    delete_button = tk.Button(task_frame, text="Remove Task", font=("Arial", 12, "bold"), command=delete_task, bg="#AA4444", fg="#FFFFFF")
    delete_all_button = tk.Button(task_frame, text="Remove All", font=("Arial", 12, "bold"), command=delete_all_tasks, bg="#BB6622", fg="#FFFFFF")
    exit_button = tk.Button(task_frame, text="Done", font=("Arial", 12, "bold"), command=close_app, bg="#882244", fg="#FFFFFF")

    add_button.grid(row=1, column=0, padx=10, pady=5)
    delete_button.grid(row=2, column=0, padx=10, pady=5)
    delete_all_button.grid(row=3, column=0, padx=10, pady=5)
    exit_button.grid(row=4, column=0, padx=10, pady=5)

    task_list = tk.Listbox(content_frame, font=("Calibri", 14), width=25, height=12, bg="#334455", fg="#FFFFFF", selectbackground="#557799")
    task_list.pack(side="right", padx=20, pady=20)

    root.protocol("WM_DELETE_WINDOW", close_app)
    root.mainloop()
