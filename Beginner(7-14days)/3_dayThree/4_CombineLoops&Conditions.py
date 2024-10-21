week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Sartaday", "Sunday"]

has_eggs = True
has_bread = False

for day in week:
    print(f"Planning for {day}:")

    if has_eggs and has_bread:
        print("you can have an egg sandwich!")
    elif has_eggs:
        print("You can have scammbled eggs!")
    elif has_bread:
        print("You can have toast")
    else:
        print("Time for grocery shopping!")
    
    print()