import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Grid layout ")

#creat labels and entry
tk.Label(root,text="Name:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=0, column=1)

tk.Label(root,text="Email:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(root).grid(row=1, column=1)


#button
submit_button = tk.Button(root, text="submit")
submit_button.grid(row=2, column=1, pady=20)

root.mainloop()