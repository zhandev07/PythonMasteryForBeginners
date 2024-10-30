import tkinter as tk

def on_hover(event):
    custom_button.config(bg="#3e8e41")  # Darker shade when hovered

def on_leave(event):
    custom_button.config(bg=button_bg)  # Original color when mouse leaves

root = tk.Tk()
root.geometry("300x200")
root.title("Interactive Feedback")

# Button with hover effect
button_bg = "#4CAF50"
custom_button = tk.Button(root, text="Hover Me", bg=button_bg, fg="white", font=("Verdana", 14, "bold"))
custom_button.pack(pady=20)

# Binding hover events to the button
custom_button.bind("<Enter>", on_hover)
custom_button.bind("<Leave>", on_leave)

def create_tooltip(widget, text):
    tooltip = tk.Toplevel(widget)
    tooltip.wm_overrideredirect(True)
    tooltip_label = tk.Label(tooltip, text=text, background="yellow", fg="black", bd=1, relief="solid")
    tooltip_label.pack()
    
    def show_tooltip(event):
        x = event.x_root + 10
        y = event.y_root + 10
        tooltip.wm_geometry(f"+{x}+{y}")
        tooltip.deiconify()
    
    def hide_tooltip(event):
        tooltip.withdraw()
    
    tooltip.withdraw()  # Start hidden
    widget.bind("<Enter>", show_tooltip)
    widget.bind("<Leave>", hide_tooltip)

# Example with tooltip
entry = tk.Entry(root, font=("Arial", 14))
entry.pack(pady=20)
create_tooltip(entry, "Enter your text here.")

root.mainloop()
