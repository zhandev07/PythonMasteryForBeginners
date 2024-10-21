# We use comparison operators to compare values. Here are some common ones:
#common operators are:
# == (equals to)
# != (not equal to)
# > (greater than)
# < (less than)
# >= (greater than or equal to)
# <= (less than or equal to)

#example compare Numbers:

#print directy
age = 18

if age >= 18:
    print("you are an adult!")
else:
    print("you are still a minor")

#ask user to input the data
use_age = int(input("Enter your Age (eg 12, 20..):"))

if use_age >= 18:
    print("you are an adult!")
else:
    print("You are still a minor.")


#Home work
# Write a program that asks the user for their age. If they are 18 or older, print a message saying they can vote. If they are younger than 18, print how many years they have left until they can vote.