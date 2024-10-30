import tkinter as tk

# Function to handle login
def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "password":
        result_label.config(text="Login Successful", fg="green")
    else:
        result_label.config(text="Invalid Credentials", fg="red")

root = tk.Tk()
root.geometry("400x300")
root.title("Login Form")

# Username label and entry
username_label = tk.Label(root, text="Username:", font=("Arial", 14))
username_label.pack(pady=10)

username_entry = tk.Entry(root, font=("Arial", 14))
username_entry.pack(pady=5)

# Password label and entry
password_label = tk.Label(root, text="Password:", font=("Arial", 14))
password_label.pack(pady=10)

password_entry = tk.Entry(root, show="*", font=("Arial", 14))
password_entry.pack(pady=5)

# Submit button
submit_button = tk.Button(root, text="Login", command=login, font=("Arial", 14))
submit_button.pack(pady=20)

# Result label
result_label = tk.Label(root, text="", font=("Arial", 14))
result_label.pack()

root.mainloop()
