import tkinter as tk

root = tk.Tk()
root.geometry("400x300")
root.title("Checkboxes in GUI")

#variable to atore check box state 
option1 = tk.IntVar()
option2 = tk.IntVar()

#create a checkboxes 
checkbox1 = tk.Checkbutton(root, text="Option 1", variable=option1)
checkbox1.pack(pady=10)

checkbox2 = tk.Checkbutton(root, text="Option 1", variable=option2)
checkbox2.pack(pady=10)

# Function to display checkbox options
def show_selections():
    result = f"option 1: {option1.get()}, Option 2: {option2.get()}"
    result_label.config(text=result)

# Button to trigger show selections
button = tk.Button(root, text="submit", command=show_selections)
button.pack(pady=10)

#dispyal the result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()