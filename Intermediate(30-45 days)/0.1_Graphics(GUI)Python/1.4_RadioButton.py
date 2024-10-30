import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Radio Button Example")

# Variable to store selected radio button value
selected_option = tk.StringVar()

# Create Radio Buttons
radio1 = tk.Radiobutton(root, text="Option A", variable=selected_option, value="A")
radio1.pack(pady=10)

radio2 = tk.Radiobutton(root, text="Option B", variable=selected_option, value="B")
radio2.pack(pady=10)

# Function to show the selected option
def show_selection():
    result_label.config(text=f"Selected: {selected_option.get()}")

# Button to show selection
button = tk.Button(root, text="Submit", command=show_selection)
button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
