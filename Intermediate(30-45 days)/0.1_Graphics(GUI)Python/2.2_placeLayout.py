import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Place Layout Example")

# Label and Button with exact positioning
label = tk.Label(root, text="Hello, Tkinter!")
label.place(x=50, y=10)


root.mainloop()