# How many days until your birthday? 
# this task is introduce you to next day of coding it complex because it involve if and else
# just reiview before next learning of code how we going to do
from datetime import datetime

#ask user for their birdt day 
birthday_day = int(input("Enter the day of your birthday:"))
birthday_month = int(input("Enter the month of your birthday:"))

#get the current time
today = datetime.today()

#create a birthdady date for current year
birthday_this_year = datetime(today.year, birthday_month, birthday_day)

#if the birthday has already pass this year, caclulate for next year
if birthday_this_year < today:
    birthday_next_year = datetime(today.year + 1, birthday_month, birthday_day)
    days_until_birthday = (birthday_next_year - today).days
else:
    days_until_birthday = (birthday_this_year -today).days

#print number left
print(f"There are {days_until_birthday} days left until your birthday!")


#get the age 

# get_today_year = datetime.today()

# Bithday_year = int(input("Enter the Bithday year:"))

# Age = (get_today_year.year) - Bithday_year

# print("you are", Age, "years old.")