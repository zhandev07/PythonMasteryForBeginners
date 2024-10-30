import os
import requests
import tkinter as tk
from dotenv import load_dotenv

#load the env variable form .env
load_dotenv()
api_key = os.getenv('OPEN_WEATHER_KEY')

#initialize the main window
root = tk.Tk()
root.title("Weather Checker")
root.geometry("400x300")

#functions to fetch the weather
def get_weather():
    city = city_entry.get().strip()
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        # Make a GET requirest to the API
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            temperature = data['main']['temp'] - 273.15 
            weather_desc = data['weather'][0]['description'].capitalize()
            result_label.config(text=f"Temperatuer: {temperature:.2f}°C\nWeather: {weather_desc}")
        
        elif response.status_code == 404:
            result_label.config(text="City not found. Please check the spelling")
        elif response.status_code == 401:
            result_label.config(text="Invalid API key. Please check the API correct")
        elif response.status_code == 429:
            result_label.config(text="Rate limit exceeded. Please subscrible to new plan!")
        else:
            result_label.config(text="Error: Could not . could not retrive data")   

    except requests.exceptions.RequestException as e:
        result_label.config(text="Network error> please try again")


# Set up the UI
city_label = tk.Label(root, text="Enter city name:")
city_label.pack()
city_entry = tk.Entry(root)
city_entry.pack()
get_weather_button = tk.Button(root, text="Get weather", command=get_weather)
get_weather_button.pack()
result_label = tk.Label(root, text="")
result_label.pack()


# Run
root.mainloop()