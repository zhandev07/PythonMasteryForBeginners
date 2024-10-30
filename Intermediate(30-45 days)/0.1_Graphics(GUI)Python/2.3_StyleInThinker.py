import tkinter as tk
from tkinter import ttk  # for combobox

root = tk.Tk()
root.geometry("500x500")
root.title("Styled Form")

# Function to submit form data
def submit_form():
    result_label.config(text=f"Name: {entry_name.get()}\nEmail: {entry_email.get()}\nCountry: {country_var.get()}")

# ------------------------ Styles ----------------------------
# Custom Fonts
font_title = ("Helvetica", 18, "bold")
font_label = ("Arial", 12)
font_entry = ("Arial", 12)
font_button = ("Verdana", 12, "bold")

# Colors
bg_color = "#f0f0f0"  # Light background
btn_color = "#007acc"  # Button color (blue)
btn_hover_color = "#005b99"  # Hover button color
entry_bg = "#ffffff"  # Entry background
entry_fg = "#333333"  # Entry text color
label_fg = "#333333"  # Label text color

# Border Radius and Relief Effect
border_width = 2
border_relief = "groove"

# ---------------------- Widgets -----------------------------

# Title Label (styled)
title_label = tk.Label(root, text="User Registration Form", font=font_title, bg=bg_color, fg=label_fg)
title_label.pack(pady=20)

# Frame to hold form elements (gives us flexibility to control layout)
form_frame = tk.Frame(root, bg=bg_color, bd=border_width, relief=border_relief, padx=20, pady=20)
form_frame.pack(padx=10, pady=10)

# Name Label and Entry
label_name = tk.Label(form_frame, text="Name:", font=font_label, bg=bg_color, fg=label_fg)
label_name.grid(row=0, column=0, padx=10, pady=10, sticky="e")
entry_name = tk.Entry(form_frame, font=font_entry, bd=border_width, bg=entry_bg, fg=entry_fg)
entry_name.grid(row=0, column=1, padx=10, pady=10)

# Email Label and Entry
label_email = tk.Label(form_frame, text="Email:", font=font_label, bg=bg_color, fg=label_fg)
label_email.grid(row=1, column=0, padx=10, pady=10, sticky="e")
entry_email = tk.Entry(form_frame, font=font_entry, bd=border_width, bg=entry_bg, fg=entry_fg)
entry_email.grid(row=1, column=1, padx=10, pady=10)

# Country Label and Combobox (Dropdown Menu)
label_country = tk.Label(form_frame, text="Country:", font=font_label, bg=bg_color, fg=label_fg)
label_country.grid(row=2, column=0, padx=10, pady=10, sticky="e")
country_var = tk.StringVar()
country_combobox = ttk.Combobox(form_frame, textvariable=country_var, values=["Tanzania", "Kenya", "Uganda", "Rwanda"], state="readonly")
country_combobox.grid(row=2, column=1, padx=10, pady=10)
country_combobox.current(0)  # Set default selection

# Submit Button
submit_btn = tk.Button(root, text="Submit", font=font_button, bg=btn_color, fg="white", bd=border_width, relief="raised", activebackground=btn_hover_color, command=submit_form)
submit_btn.pack(pady=20)

# Result Label (to show the form results)
result_label = tk.Label(root, text="", font=font_label, bg=bg_color, fg=label_fg)
result_label.pack(pady=10)

# --------------------- Start Mainloop ------------------------
root.config(bg=bg_color)  # Set root window background
root.mainloop()
