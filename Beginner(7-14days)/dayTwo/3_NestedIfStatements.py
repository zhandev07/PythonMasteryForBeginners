# Sometimes, we make decisions inside other decisions. This is called nesting.

# Deciding Based on Time and Weather
#print directy
time_of_day = "morning"
weather = "sunny"

if time_of_day == "morning":
    if weather == "sunny":
        print("Good morning! It's sunny, have a great day!")
    elif weather == "rainy":  
        print("Good morning! It's rainy, please take an umbrella.")
elif time_of_day == "afternoon":  
    if weather == "rainy":
        print("Good afternoon! It's rainy, please when you're out, take an umbrella.")
    else:
        print("Good afternoon! It's sunny, have a relaxing day.")
else: 
    print("Good evening! Don't forget to close the water pump!")  


#ask user to input data
Time_day_input = input("Enter a time of a day eg morning ... :")

weather_input = input("Enter a weather conditions eg sunny,rainy:")

if Time_day_input == "morning":
    if weather_input == "sunny":
        print("Good morning! It's sunny, have a great day!")
    elif weather_input == "rainy":  
        print("Good morning! It's rainy, please take an umbrella.")
elif Time_day_input == "afternoon":  
    if weather_input == "rainy":
        print("Good afternoon! It's rainy, please when you're out, take an umbrella.")
    else:
        print("Good afternoon! It's sunny, have a relaxing day.")
else: 
    print("Good evening! Don't forget to close the water pump!")  

