# Handling Non-Existent Files (more we will lrean on day 7)
try:
    with open("helloworld.text", "r") as file:
        content = file.read()
except FileNotFoundError:
    print("The file you are trying to open doesn't exist.")