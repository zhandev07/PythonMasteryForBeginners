import tkinter as tk

root = tk.Tk()
root.geometry("300x200")

# Using grid for a responsive form layout
label_name = tk.Label(root, text="Name:")
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")

entry_name = tk.Entry(root)
entry_name.grid(row=0, column=1, padx=10, pady=10)

label_email = tk.Label(root, text="Email:")
label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_email = tk.Entry(root)
entry_email.grid(row=1, column=1, padx=10, pady=10)

submit_button = tk.Button(root, text="Submit")
submit_button.grid(row=2, column=0, columnspan=2, pady=20)

root.mainloop()
