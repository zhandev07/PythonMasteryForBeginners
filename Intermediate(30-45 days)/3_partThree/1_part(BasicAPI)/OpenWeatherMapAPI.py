import os
import requests
from tkinter import *
from dotenv import load_dotenv

# Load the environment variables from .env file
load_dotenv()

# Get API key from the environment variable
api_key = os.getenv('OPEN_WEATHER_KEY')

# Function to fetch weather data
def get_weather():
    city = city_entry.get()  # Get the city from the user input

    # API URL
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"
    
    # Send GET request to the API
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        
        # Extract temperature (in Celsius) and weather description
        temperature = data['main']['temp'] - 273.15  # Convert from Kelvin to Celsius
        weather_description = data['weather'][0]['description'].capitalize()
        
        # Display the weather information in the result label
        result_label.config(text=f"Temperature: {temperature:.2f}°C\nWeather: {weather_description}")
    else:
        result_label.config(text="Error: Could not retrieve data")

# Set up the GUI
root = Tk()
root.title("Weather Checker")
root.geometry("400x250")

# Create GUI elements
city_label = Label(root, text="Enter city name", font=("Courier New", 18))
city_label.pack(pady=10)

city_entry = Entry(root, width=35)
city_entry.pack(pady=5)

get_weather_button = Button(root, text="Get Weather", command=get_weather)
get_weather_button.pack(pady=10)

result_label = Label(root, text="")
result_label.pack(pady=20)

# Start the Tkinter main loop
root.mainloop()
