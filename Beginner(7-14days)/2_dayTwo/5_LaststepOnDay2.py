###############################################
########## SAMPLE PROJECT IN DAY 2###############
########################################

# # 3. Can You Vote?
# #ask use input
Age_input = int(input("Enter your age number:"))

remain_years = (18 - Age_input)

if Age_input >= 18:
    print("You can vote!.")
else:
    print("Your have remain", remain_years, "year's to vote")


# 4. Movie Time
Movie_ticket = input("Do you have a Movie ticket!:")
Money_for_snack = input("Do you have enough money for snacks!:")

if Movie_ticket == "yes" and Money_for_snack == "yes":
    print("Enjoy the movie and snacks")
elif Movie_ticket == "yes":
    print("Enjoy the movie")
elif Money_for_snack == "yes":
    print("You can't watch movie, but at least you can have snacks")
else:
    print("Maybe Next time!")

# 5 Virtual Shopping Assistant?
user_budget = float(input("Enter your burget in (Tsh)!:"))

#input the prices of 3 items they wants to buy.
items_one = float(input("Enter the price of item one!:"))
items_two = float(input("Enter the price of item two!:"))
items_three = float(input("Enter the price of item three!:"))

More_money = ((items_one + items_two + items_three) - user_budget)

if user_budget >= (items_one + items_two + items_three):
    print("You can buy all items")
else:
    print("You need more money which is", More_money , "To buy all items")

# 6 Grade Calculator
grade = int(input("Enter a grade!eg 20)"))

if grade >= 90:
    print("you got A")
elif grade >= 80:
    print("you got B")
elif grade >= 70:
    print("you got C")
elif grade >= 60:
    print("you got D")
elif grade <= 60:
    print ("you got F")

