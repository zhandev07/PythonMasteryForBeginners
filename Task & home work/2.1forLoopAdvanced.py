# Write a program that:

# Asks the user how many pets they have.
# Asks for the name of each pet and its type (e.g., dog, cat).
# Stores this information in a list of lists.
# Loops through the list and prints something like:
# "Pet #1 is a dog named Bella".

num_pets = int(input("Enter a number of pets you have!:"))

pets = []

for i in range(num_pets):
    pet_name = input(f"Enter name of a pet #{i+1}: ")
    pet_type = input(f"Enter the type of a pets #{i+1}: ")
    pets.append([pet_name, pet_type])

for index, pet_info in enumerate(pets):
    pet_name, pet_type = pet_info
    print(f"Pet #{index+1} is a {pet_type} named {pet_name}")

# Write a program that asks the user to input 5 different colors.
# Loop through the list of colors and print each color, but stop the loop if the color "red" is entered.

colors = []
for i in range(5):
    User_input = input(f"Enter different color name #{i+1}: ")
    colors.append(User_input)

for color in colors:
    if color.lower() == "red":
        print("Red found")
        break
    print(color)
