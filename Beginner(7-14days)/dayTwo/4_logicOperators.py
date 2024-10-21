  # Logical operators:
# and: Both conditions must be true.
# or: At least one condition must be true.
# not: Reverses the condition.

#combine conditins
#example 1
day_of_week = "Friday"
weather = "sunny"

if day_of_week == "Friday" and weather == "sunny":
    print("It's a sunny Friday! Time for a picnic!")
elif day_of_week == "Friday" or weather == "sunny":
    print("At least it's ether Friday or sunny")
else:
    print("It's neither sunny nor Friday")

#example 2
# Deciding What to Cook
has_eggs = True
has_bread = False

if has_eggs and has_bread:
    print("You can make an egg sandwich!")
elif has_eggs:
    print("you can make Scrambled eggs!")
elif has_bread:
    print("you can make toast!")
else:
    print("Looks like it's time to go grocery shopping!")