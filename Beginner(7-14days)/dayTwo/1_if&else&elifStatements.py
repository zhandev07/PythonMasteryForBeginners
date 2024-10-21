#decide what to wear

#print directy
weather = "sunny"

if weather == "sunny":
    print("It's sunny! Wear Sunglasses!")
elif weather == "rainy":
    print("It's rainy! Take an Umbrella")
else:
    print("Weather is fine. Dress normally")

#ask user to input 
weather_input = input("Enter the weather:")

if weather_input == "sunny":
    print("It's sunny! Wear sunglasses!")
elif weather_input == "rainy":
    print("It's rainly! Take an umbrella!")
else:
    print("Weather is fine. Dress normally")