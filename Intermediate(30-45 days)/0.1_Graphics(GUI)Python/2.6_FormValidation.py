import re  # For regular expressions
import tkinter as tk


def validate_email():
    email = entry_email.get()
    if re.match(r"[^@]+@[^@]+\.[^@]+", email):  # Simple email regex
        result_label.config(text="Valid Email!", fg="green")
    else:
        result_label.config(text="Invalid Email!", fg="red")

root = tk.Tk()
root.geometry("300x200")
root.title("Form Validation Example")

# Email Entry
entry_email = tk.Entry(root, font=("Arial", 14))
entry_email.pack(pady=20)

# Validate Button
validate_button = tk.Button(root, text="Validate Email", command=validate_email)
validate_button.pack()

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
