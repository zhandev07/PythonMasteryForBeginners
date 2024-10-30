# Define rooms as dictionaries
rooms = {
    "Entrance": {
        "description": "You are at the entrance of a dark cave.",
        "exits": {"north": "Hallway"},
        "items": ["flashlight"]
    },
    "Hallway": {
        "description": "A long hallway with doors to the east and west.",
        "exits": {"south": "Entrance", "east": "Treasure Room"},
        "items": []
    },
    "Treasure Room": {
        "description": "You've found the treasure room!",
        "exits": {"west": "Hallway"},
        "items": ["gold coin", "ancient relic"]
    }
}

# Player's inventory
inventory = []

def show_room(room_name):
    room = rooms[room_name]
    print(room["description"])
    print("Exits:", ', '.join(room["exits"].keys()))
    if room["items"]:
        print("You see:", ', '.join(room["items"]))

def move_to_room(current_room, direction):
    if direction in rooms[current_room]["exits"]:
        return rooms[current_room]["exits"][direction]
    else:
        print("You can't go that way!")
        return current_room

def collect_item(current_room):
    room = rooms[current_room]
    if room["items"]:
        item = room["items"].pop(0)  # Collect first item
        inventory.append(item)
        print(f"You collected: {item}")
    else:
        print("No items here!")

def show_inventory():
    if inventory:
        print("Your inventory:", ', '.join(inventory))
    else:
        print("Your inventory is empty.")

def main():
    current_room = "Entrance"
    while True:
        show_room(current_room)
        action = input("What would you like to do? (move, collect, inventory, quit) ").strip().lower()

        if action == "move":
            direction = input("Which direction? ").strip().lower()
            current_room = move_to_room(current_room, direction)
        elif action == "collect":
            collect_item(current_room)
        elif action == "inventory":
            show_inventory()
        elif action == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid action!")

if __name__ == "__main__":
    main()
