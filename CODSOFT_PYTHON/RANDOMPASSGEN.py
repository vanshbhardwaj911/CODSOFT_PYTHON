import random
import string
import tkinter as tk
from tkinter import messagebox

def generate_random_password():
    password_length = password_length_var.get()
    password_complexity = password_complexity_var.get()

    if not password_length.isdigit() or int(password_length) <= 0:
        messagebox.showerror("Error", "Invalid input for password length.")
        return

    password_length = int(password_length)

    if password_complexity == "Basic":
        password_chars = string.ascii_letters
    elif password_complexity == "Moderate":
        password_chars = string.ascii_letters + string.digits
    else:
        password_chars = string.ascii_letters + string.digits + string.punctuation

    random_password = "".join(random.choice(password_chars) for _ in range(password_length))
    random_password_var.set(random_password)

def copy_password_to_clipboard():
    random_password = random_password_var.get()
    if random_password:
        root.clipboard_clear()
        root.clipboard_append(random_password)
        messagebox.showinfo("Copied", "Password copied!")

def reset_password():
    random_password_var.set("")
    password_length_var.set("")
    password_complexity_var.set("Basic")

root = tk.Tk()
root.title("Random Password Generator")
root.geometry("400x400")
root.configure(bg="#0E1E24")

frame = tk.Frame(root, bg="#0E1E24")
frame.pack(pady=20)

greeting_label = tk.Label(frame, text="Hello User!", font=("Helvetica", 16, "bold"), fg="#FFFFFF", bg="#0E1E24")
greeting_label.grid(row=0, columnspan=2)

tk.Label(frame, text="Password Limit:", font=("Helvetica", 12), fg="#FFFFFF", bg="#0E1E24").grid(row=1, column=0)
password_length_var = tk.StringVar()
password_length_entry = tk.Entry(frame, textvariable=password_length_var, width=10)
password_length_entry.grid(row=1, column=1)

tk.Label(frame, text="Complexity Level:", font=("Helvetica", 12), fg="#FFFFFF", bg="#0E1E24").grid(row=2, column=0)
complexity_choices = ["Level 1", "Level 2", "Level 3"]
password_complexity_var = tk.StringVar()
complexity_menu = tk.OptionMenu(frame, password_complexity_var, *complexity_choices)
complexity_menu.grid(row=2, column=1)

generate_button = tk.Button(root, text="Generate Password", command=generate_random_password, bg="#329932", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
generate_button.pack()

password_frame = tk.Frame(root, bg="#0E1E24")
password_frame.pack(pady=10)

password_label = tk.Label(password_frame, text="Generated Password:", font=("Helvetica", 12), fg="#FFFFFF", bg="#0E1E24")
password_label.pack()
random_password_var = tk.StringVar()
password_display = tk.Label(password_frame, textvariable=random_password_var, fg="#FFFFFF", bg="#0E1E24", font=("Courier New", 14, "bold"))
password_display.pack(pady=5)

copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_password_to_clipboard, bg="#E57D4B", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
copy_button.pack()

reset_button = tk.Button(root, text="Reset", command=reset_password, bg="#E53935", fg="#FFFFFF", font=("Helvetica", 12, "bold"))
reset_button.pack()

farewell_label = tk.Label(root, text="Thanks for using me.", font=("Helvetica", 10), fg="#FFFFFF", bg="#0E1E24")
farewell_label.pack(pady=20)

root.mainloop()
