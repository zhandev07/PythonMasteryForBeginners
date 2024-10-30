import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def get_stock_price():
    # Get the stock symbol from the entry field
    symbol = entry_symbol.get().upper()
    url = f'https://finance.yahoo.com/quote/{symbol}'
    
    # Send the request to Yahoo Finance
    response = requests.get(url)
    
    # Check for successful response
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            # Find the stock price using BeautifulSoup
            price_tag = soup.find('fin-streamer', {'data-field': 'regularMarketPrice'})
            if price_tag and price_tag.text:  # Ensure price_tag is not None and has text
                stock_price = price_tag.text
                label_result.config(text=f"{symbol} Price: {stock_price} USD")
            else:
                raise AttributeError("Price tag not found")  # Raise an error if price tag is missing
        except AttributeError:
            messagebox.showerror("Error", "Could not find stock price. Check symbol and try again.")
    else:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection or try again later.")

# GUI Setup
app = tk.Tk()
app.title("Stock Price Checker")
app.geometry("350x200")

# Label for title
label_title = tk.Label(app, text="Enter Stock Symbol", font=("Helvetica", 14))
label_title.pack(pady=10)

# Entry for stock symbol
entry_symbol = tk.Entry(app, font=("Helvetica", 12))
entry_symbol.pack(pady=5)

# Button to fetch stock price
button_get_price = tk.Button(app, text="Get Stock Price", command=get_stock_price)
button_get_price.pack(pady=10)

# Label to display results
label_result = tk.Label(app, text="", font=("Helvetica", 12))
label_result.pack(pady=20)

app.mainloop()
