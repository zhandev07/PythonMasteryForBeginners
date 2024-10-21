#1 Looping Through Strings

worlds = "Python"

for letter in worlds:
    print(letter)

# 2. break and continue Keywords


#let start with break
friends = ["python", "php", "java"]

for friend in friends:
    if friend == "php":
        break
    print(friend)



#let  check continue keyword
for friend in friends:
    if friend == "php":
        continue
    print(friend)

# 3. Looping with enumerate()

for index, friend in enumerate(friends):
    print(f"Friend #{index+1} is {friend}")

# 4. Looping Through a List of Lists
friends_and_ages = [["python", 8], ["php", 12], ["java", 15]]

for agefriend in friends_and_ages:
    name, age = agefriend
    print(f"{name} is {age} years old as programming languange")

# 5. Looping in Reverse with reversed()
for friend in reversed(friends):
    print(friend)

# 6. Looping Through Dictionaries

ages_friends = {"Python": 8, "php": 12, "java": 15}

for name, age in ages_friends.items():
    print(f"{name} is {age} years old as programming")