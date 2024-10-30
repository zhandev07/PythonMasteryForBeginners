import tkinter as tk

root = tk.Tk()
root.geometry("300x200")
root.title("Custom Widgets Example")

# Custom Fonts and Colors
custom_font = ("Verdana", 14, "bold")
button_bg = "#4CAF50"  # Green background
button_fg = "white"    # White text
label_bg = "#f0f0f0"   # Light grey label background
label_fg = "#333333"   # Dark grey text

# Custom Button
custom_button = tk.Button(root, text="Click Me", font=custom_font, bg=button_bg, fg=button_fg, bd=3, relief="raised")
custom_button.pack(pady=20)

# Custom Label
custom_label = tk.Label(root, text="This is a custom label!", font=custom_font, bg=label_bg, fg=label_fg, bd=2, relief="solid")
custom_label.pack(pady=20)

root.mainloop()
