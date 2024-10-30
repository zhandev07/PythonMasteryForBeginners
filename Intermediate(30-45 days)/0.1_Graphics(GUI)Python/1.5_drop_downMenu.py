import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Dropdown Example")

# List of options
options = ["Python", "Java", "C++", "JavaScript"]

# Variable to store the selected option
selected_option = tk.StringVar()
selected_option.set(options[0])  # Set default value

# Create Dropdown (OptionMenu)
dropdown = tk.OptionMenu(root, selected_option, *options)
dropdown.pack(pady=20)

# Function to show selected option
def show_selection():
    result_label.config(text=f"Selected: {selected_option.get()}")

# Button to submit
submit_button = tk.Button(root, text="Submit", command=show_selection)
submit_button.pack(pady=10)

# Result Label
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
