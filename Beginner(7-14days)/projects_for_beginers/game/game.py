import json
import random
import os
import pygame  # For sound effects
import tkinter as tk  # For GUI

# Initialize pygame mixer for sound effects
pygame.mixer.init()
positive_sound1 = r"C:\Users\lucian\Desktop\python\Beginner(7-14days)\projects_for_beginers\game\sound\positive_effect.wav"
negative_sound2 = r"C:\Users\lucian\Desktop\python\Beginner(7-14days)\projects_for_beginers\game\sound\negative_effect.wav"
background_music3 = r"C:\Users\lucian\Desktop\python\Beginner(7-14days)\projects_for_beginers\game\sound\background_music.wav"

# Load sound effects
def load_sounds():
    global positive_sound, negative_sound, background_music
    positive_sound = pygame.mixer.Sound(positive_sound1)  # Replace with your sound file
    negative_sound = pygame.mixer.Sound(negative_sound2)  # Replace with your sound file
    background_music = pygame.mixer.Sound(background_music3)  # Replace with your music file
    background_music.play(-1)  # Play background music in a loop

# Function to display the introduction
def introduction():
    print("Welcome to the Love Story Adventure!")
    print("In this game, you will make choices that influence your love story.")
    print("Let's create your character first!")
    name = input("Enter your character's name: ")
    attributes = {
        'charm': random.randint(1, 10),
        'intelligence': random.randint(1, 10),
        'empathy': random.randint(1, 10)
    }
    return name, attributes

# Function to get the difficulty level
def choose_difficulty():
    print("\nChoose your difficulty level:")
    print("1. Simple")
    print("2. Medium")
    print("3. Hard")
    while True:
        choice = input("Enter your choice (1-3): ")
        if choice in ['1', '2', '3']:
            return choice
        else:
            print("Invalid input. Please enter 1, 2, or 3.")

# Function to track emotional responses
def emotional_response(feelings):
    print("\nYour emotional state:")
    for emotion, value in feelings.items():
        print(f"{emotion.capitalize()}: {value}")
    if feelings['happiness'] > 70:
        print("You feel incredibly happy and in love!")
    elif feelings['happiness'] > 40:
        print("You're feeling good about your relationship.")
    else:
        print("You might need to rethink your choices...")

# Function to save player data
def save_game(player_id, name, attributes, feelings, inventory):
    game_data = {
        'player_id': player_id,
        'name': name,
        'attributes': attributes,
        'feelings': feelings,
        'inventory': inventory
    }
    with open(f'{player_id}_saved_game.json', 'w') as f:
        json.dump(game_data, f)
    print("Game saved successfully!")

# Function to load player data
def load_game(player_id):
    file_name = f'{player_id}_saved_game.json'
    if os.path.exists(file_name):
        with open(file_name, 'r') as f:
            game_data = json.load(f)
        print("Game loaded successfully!")
        return game_data['name'], game_data['attributes'], game_data['feelings'], game_data['inventory']
    else:
        print("No saved game found.")
        return None, None, None, None

# Function for main game loop
def play_game(name, attributes, difficulty, inventory):
    feelings = {'happiness': 50, 'sadness': 0, 'anger': 0}  # Initial emotional state
    story_paths = {
        'simple': [
            ("You see someone interesting at a café. Do you want to (1) say hi or (2) ignore them?", 
             "You decided to say hi! They smile back. Your happiness increases by 10!", 
             "You chose to ignore them. You feel a bit sad about missing the chance. Your sadness increases by 5."),
            ("You find a love letter. Do you (1) read it or (2) throw it away?", 
             "Reading the letter brings you joy! Your happiness increases by 15.", 
             "You miss out on something special. Your sadness increases by 5.")
        ],
        'medium': [
            ("You meet someone at a party. Do you (1) dance with them or (2) talk to someone else?", 
             "Dancing with them was fun! Your happiness increases by 20.", 
             "Talking to someone else makes you feel left out. Your happiness decreases by 10. Your sadness increases by 5."),
            ("You receive a special gift. Do you (1) accept it or (2) refuse it?", 
             "Accepting the gift boosts your mood! Your happiness increases by 25.", 
             "Refusing the gift leaves you feeling regretful. Your sadness increases by 10.")
        ],
        'hard': [
            ("You have a date planned, but they cancel last minute. Do you (1) confront them or (2) give them space?", 
             "Confronting them makes things worse. Your happiness decreases by 30. Your anger increases by 15.", 
             "Giving them space shows maturity. Your happiness increases by 10."),
            ("You hear a rumor about your partner. Do you (1) confront them or (2) trust them?", 
             "Confronting them leads to an argument. Your happiness decreases by 20. Your anger increases by 10.", 
             "Trusting them strengthens your bond. Your happiness increases by 20.")
        ]
    }

    # Select the story path based on difficulty
    path = story_paths['simple'] if difficulty == '1' else (story_paths['medium'] if difficulty == '2' else story_paths['hard'])

    # Game loop
    for prompt, choice1, choice2 in path:
        print("\n" + prompt)
        while True:
            choice = input("Enter your choice (1 or 2): ")
            if choice == '1':
                feelings['happiness'] += 10 if difficulty == '1' else (20 if difficulty == '2' else -30)
                feelings['sadness'] -= 5 if feelings['sadness'] > 0 else 0  # Decrease sadness if positive choice
                print(choice1)
                inventory.append("Positive Item")  # Example of adding an item to the inventory
                positive_sound.play()  # Play positive sound
                break
            elif choice == '2':
                feelings['happiness'] -= 10 if difficulty == '1' else (10 if difficulty == '2' else 30)
                feelings['sadness'] += 5  # Increase sadness
                print(choice2)
                inventory.append("Negative Item")  # Example of adding an item to the inventory
                negative_sound.play()  # Play negative sound
                break
            else:
                print("Invalid input. Please enter 1 or 2.")

    # Final emotional state
    emotional_response(feelings)
    return inventory  # Return any collected items

# Function to create or load a user account
def user_account():
    print("Do you want to (1) create a new account or (2) log in to an existing account?")
    choice = input("Enter your choice (1 or 2): ")
    
    if choice == '1':
        player_id = input("Choose a username: ")
        if not os.path.exists(f'{player_id}_saved_game.json'):
            print(f"Account '{player_id}' created successfully!")
            return player_id
        else:
            print("Username already exists. Try again.")
            return user_account()
    elif choice == '2':
        player_id = input("Enter your username: ")
        if os.path.exists(f'{player_id}_saved_game.json'):
            print(f"Logged in as '{player_id}' successfully!")
            return player_id
        else:
            print("Account does not exist. Try again.")
            return user_account()
    else:
        print("Invalid input. Please enter 1 or 2.")
        return user_account()

# Function to create a GUI for inventory display
def show_inventory(inventory):
    inventory_window = tk.Tk()
    inventory_window.title("Inventory")

    tk.Label(inventory_window, text="Your Inventory:", font=("Arial", 14)).pack()

    for item in inventory:
        tk.Label(inventory_window, text=item, font=("Arial", 12)).pack()

    tk.Button(inventory_window, text="Close", command=inventory_window.destroy).pack()
    inventory_window.mainloop()

# Main function to run the game
def main():
    load_sounds()  # Load sounds at the start
    player_id = user_account()
    name, attributes, feelings, inventory = load_game(player_id)
    if name is None:
        name, attributes = introduction()
        feelings = {'happiness': 50, 'sadness': 0, 'anger': 0}
        inventory = []

    difficulty = choose_difficulty()
    inventory = play_game(name, attributes, difficulty, inventory)

    # Show inventory using GUI
    show_inventory(inventory)

    # Save the game after playing
    save_game(player_id, name, attributes, feelings, inventory)
    print("\nThank you for playing! Hope you enjoyed your love story adventure!")

# Start the game
if __name__ == "__main__":
    main()
