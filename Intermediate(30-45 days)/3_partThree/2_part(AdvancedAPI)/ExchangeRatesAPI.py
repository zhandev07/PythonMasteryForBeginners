import os
import requests
import tkinter as tk
from tkinter import ttk  # For dropdown menus
from dotenv import load_dotenv

# Load the environment variables
load_dotenv()
api_key = os.getenv('EXCHANGE_RATE_API')

# Define the list of currencies for dropdown
currencies = ["USD", "EUR", "GBP", "JPY", "AUD", "CAD", "CHF", "CNY", "SEK", "NZD", "TZS"]  # Add more as needed

# Initialize the main window
root = tk.Tk()
root.title("Currency Converter")
root.geometry("400x350")
root.configure(bg="#000000")  # Set background color

# Function to convert currency
def convert_currency():
    base_currency = base_currency_dropdown.get().strip()
    target_currency = target_currency_dropdown.get().strip()
    amount = amount_entry.get().strip()

    if not amount.replace('.', '', 1).isdigit():
        result_label.config(text="Please enter a valid amount.")
        return
    
    url = f"https://v6.exchangerate-api.com/v6/{api_key}/pair/{base_currency}/{target_currency}"

    try:
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            conversion_rate = data['conversion_rate']
            converted_amount = float(amount) * conversion_rate
            result_label.config(text=f"{amount} {base_currency} = {converted_amount:.2f} {target_currency}")
        
        elif response.status_code == 404:
            result_label.config(text="Currency not found. Try again.")
        elif response.status_code == 401:
            result_label.config(text="Invalid API key.")
        elif response.status_code == 429:
            result_label.config(text="Rate limit exceeded. Try later.")
        else:
            result_label.config(text="Error: Unable to fetch data.")

    except requests.exceptions.RequestException:
        result_label.config(text="Network error. Check your connection.")

# Styling
style = ttk.Style()
style.configure("TLabel", font=("Arial", 12), background="#f5f5f5")
style.configure("TButton", font=("Arial", 10), padding=5)
style.configure("TEntry", padding=5)

# Labels and dropdowns
tk.Label(root, text="Base Currency:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
base_currency_dropdown = ttk.Combobox(root, values=currencies, state="readonly", width=15)
base_currency_dropdown.current(0)  # Default to the first currency
base_currency_dropdown.pack()

tk.Label(root, text="Target Currency:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
target_currency_dropdown = ttk.Combobox(root, values=currencies, state="readonly", width=15)
target_currency_dropdown.current(1)  # Default to the second currency
target_currency_dropdown.pack()

tk.Label(root, text="Amount:", font=("Arial", 12), bg="#f5f5f5").pack(pady=5)
amount_entry = ttk.Entry(root, font=("Arial", 10), width=20)
amount_entry.pack()

# Convert button and result label
convert_button = ttk.Button(root, text="Convert", command=convert_currency)
convert_button.pack(pady=10)
result_label = ttk.Label(root, text="", font=("Arial", 12), background="#f5f5f5", wraplength=300, justify="center")
result_label.pack(pady=10)

# Run the main loop
root.mainloop()
