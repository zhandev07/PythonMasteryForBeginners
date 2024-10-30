import requests
from bs4 import BeautifulSoup
import tkinter as tk
from tkinter import messagebox

def get_weather():
    city = entry_city.get().replace(" ", "-").lower()
    url = f'https://www.timeanddate.com/weather/{city}'
    response = requests.get(url)
    
    if response.status_code == 200:
        soup = BeautifulSoup(response.text, 'html.parser')
        try:
            temperature_tag = soup.find('div', class_='h2')
            temperature = temperature_tag.text.strip()
            label_result.config(text=f"Current Temp in {entry_city.get().title()}: {temperature}")
        except AttributeError:
            messagebox.showerror("Error", "Could not find weather data. Check city name and try again.")
    else:
        messagebox.showerror("Error", "Failed to retrieve data. Check your internet connection or try again later.")

# GUI Setup
app = tk.Tk()
app.title("Weather Checker")
app.geometry("350x200")

label_title = tk.Label(app, text="Enter City Name", font=("Helvetica", 14))
label_title.pack(pady=10)

entry_city = tk.Entry(app, font=("Helvetica", 12))
entry_city.pack(pady=5)

button_get_weather = tk.Button(app, text="Get Weather", command=get_weather)
button_get_weather.pack(pady=10)

label_result = tk.Label(app, text="", font=("Helvetica", 12))
label_result.pack(pady=20)

app.mainloop()
