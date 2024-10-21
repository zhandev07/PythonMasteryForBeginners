#send message to a friends

friends = ["python", "Php", "Java"]

for friend in friends:
    print(f"Hey {friend}, how are you?")


#repeat the same task but you ask user to enter data

#ask how many friends
num_of_friends = int(input("How many friends do you want to send message to ?"))

#create an empty list to store the name
friends = []

#loop to get names from the user and them to the list
for i in range(num_of_friends):
    name = input(f"Enter the name of friend #{i+1}:")
    friends.append(name) #add the name to the list

#Loop through the list and send a message to each friend

for friend in friends:
    print(f"Hey {friend}, how are you?")


