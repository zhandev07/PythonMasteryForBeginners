# 4. Check Voting Eligibility
from datetime import datetime

def vote_englibility(age, remain_time):
    if age >= 18 :
        print(f"You age is {age} you can register to vote! Goodluck")
    else:
        years_remaining = remain_time['years']
        months_remaining = remain_time['months']
        days_remaining = remain_time['days']
        
        print(f"Sorry you age is {age}! you can't vote yet")
        print(f"You need to wait {years_remaining} years, {months_remaining} months, and {days_remaining} days to be eligible to vote.")
        print("Be patient, and you are welcome to vote when you're old enough!")

#ask user to input birthday
user_year = int(input("Enter your birth year (e.g. 2000): "))
user_month = int(input("Enter your birth month (e.g. 01 for January): "))
user_day = int(input("Enter your birth day (e.g. 02): "))

#Get today's date
today = datetime.today()

#calculate the user's birtdate
birthdate = datetime(user_year, user_month, user_day)

#calulate the age on the year
age = today.year - birthdate.year

#check uf user hasn't had their birthday yet this year
if(today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1 # Reduce age by 1 if birthday hasn't happened yet this year

#if user is under 18 calculate the remain time
if age < 18:
    #the date where the turn 18
    eighteenth_birthday = datetime(user_year + 18, user_month, user_day)

    #cacl the defference btn now and their 18th birthday
    remaining_time = eighteenth_birthday - today
    years_remaining = remaining_time.days // 365   # Approximate years remaining
    months_remaining = (remaining_time.days % 365) // 30 # Approximate months remaining
    days_remaining = (remaining_time.days % 365) % 30 # Approximate days remaining

    #pack the remaining time in dictionary for easy access 
    #dictionary will be on day 5 dont worry just see you will learn on day 5
    remaining_time_dict = {
        'years': years_remaining,
        'months': months_remaining,
        'days': days_remaining
    } 
else:
    remaining_time_dict = {
        'years': 0,
        'months': 0,
        'days': 0
    }

vote_englibility(age, remaining_time_dict)