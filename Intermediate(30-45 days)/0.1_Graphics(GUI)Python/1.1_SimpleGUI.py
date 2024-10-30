import tkinter as tk

#create the main window
window = tk.Tk()
window.title("My First GUI")

window.geometry("400x300")

# Step 1: Create a Label widget
label = tk.Label(window, text="Welcome to Python GUI!", font=("Arial", 20))

# Step 2: Add the Label to the window
label.pack()

# step 1: create a Entry widget
entry = tk.Entry(window, font=("Courier New", 14))

# step 2: add the Entry to the window
entry.pack()

#create a button
def on_click():
    print("Button Clicked!")

# Step 1: Create a Button widget
button = tk.Button(window, text="Click Me", command=on_click)

# Step 2: Add the Button to the window
button.pack()

# Getting Text from Entry:
def show_input():
    user_input = entry.get() #get the text
    print(f"You entered: {user_input}")

# create an entry widget
entry = tk.Entry(window, font=("Latin", 12))
entry.pack()

# Create a Button to submit the text
submit_button = tk.Button(window, text="Submit", fg='white', bg="black", command=show_input)
submit_button.pack()

#run the GUI app
window.mainloop()