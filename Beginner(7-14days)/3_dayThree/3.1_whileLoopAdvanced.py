# 1 Combining Concepts: Nesting Loops and Conditionals

correct_password = "python"
password_attempt = ""
attemps = 3

while password_attempt != correct_password and attemps > 0 :
    password_attempt = input(f"Enter your password (Attempt left: {attemps}): ")
    attemps -= 1

if password_attempt.lower() == correct_password:
    print("Access Granted!")
else:
    print("Access Denied. No more attemps left.")


# 2 Guessing Game

secret_number = 5
guess = 0

while guess != secret_number:
    guess = int(input("Guess the secret number (1-10): "))
    if guess < secret_number:
        print("Too low! Try agin")
    elif guess > secret_number:
        print("Too high! try again")
    
print("Congatulation! you've guessed the secret number!")

#Simple ATM
balance = 10000.00  #starting balance

while balance> 0:
    withdrawal = float(input("Enter the amount to withdrwa: Tsh"))
    if withdrawal > balance:
        print("Insuffient funds! Try a smaller amount")
    else:
        balance -= withdrawal
        print(f"You have withdrawn: Tsh{withdrawal}")
        print(f"Remain balance: Tsh{balance}")
print("No balance left! Please deposit money")