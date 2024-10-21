balance = 0 #starting balance
pin = "1234" #default pin for login
transaction_history = [] #list od store info trans

def login():
    """Enter the PIN For Login"""

    for _ in range(5):
        entered_pin = input("Please enter your PIN: ")
        if entered_pin == pin:
            print("Login Sucessfull")
            return True
        else:
            print(f"Incorrect PIN. Try again #{_+1}")
    print("Too many incorrect attempts. Sorry contact us!")
    return False

def check_balance():
    """Display the Current Balance"""
    login()
    print(f"your balance is Tsh {balance:.2f}")

def deposit_money():
    """Hi customer! Deposit Money here"""
    global balance  # Allows us to modify the global balance variable
    try:
       amount = float(input("Enter the deposit amount: "))
       if amount > 0:
           balance += amount
           transaction_history.append(f"Deposit: Tsh{amount:.2f}, Balance: Tsh{balance:.2f}")
           print(f"Tsh{amount:.2f} deposited. New balance : Tsh{balance:.2f}")
       else:
           print("Deposited amount must me positive eg +1,2...")
    except ValueError:
        print("Invalid input. Please enter valid amount number!")

def withdraw_money():
     """Hi customer! Withdraw Money here"""
     global balance  # Allows us to modify the global balance variable
     try:
        amount = float(input("Enter the Withdrawal amount: "))
        if amount > balance:
            print("Insufficient balance!")
        elif amount <= 0:
            print("Withdraw amount must me positive eg +1,2...")
        else:
            balance -= amount
            transaction_history.append(f"Withdraw: Tsh{amount:.2f}, Balance: Tsh{balance:.2f}")
            print(f"Tsh{amount:.2f} Withdraw. New balance : Tsh{balance:.2f}")
            
     except ValueError:
        print("Invalid input. Please enter valid amount number!")

def view_teansaction_history():
    """Display the transaction History"""
    if not transaction_history:
        print("No transactions made yet.")
    else:
        print("Transaction History:")
        for transaction in transaction_history:
            print(transaction)

def calculate_interest(rate, years):
    """Calculate interest on the current balance"""
    global balance
    interest = balance * (rate / 100) * years
    balance += interest
    transaction_history.append(f"Interest added: Tsh{interest:.2f}, Balance: Tsh{balance:.2f} ")
    print(f"Interest of Tsh{interest:.2f} added for {years} years at {rate}%. New balance: Tsh{balance:.2f}")

def currency_conversion(conversion_rate, target_currency):
    """Convert the current balance to another currency"""
    conveted_amount = balance * conversion_rate
    print(f"Your Balance in {target_currency} is : {conveted_amount:.2f} {target_currency}")

def show_menu():
    """Main menu"""
    print("\nWelcome to the Python Banking System!")
    print("Please select an option:")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. View Transaction History")
    print("5. Calculate Interest")
    print("6. Convert Currency")
    print("7. Exit")

def ussd_menu():
    """ USSD menu system """
    if login():
        while True:
            show_menu()
            option = input("\nEnter number (1-7): ")

            if option == "1":
                check_balance()
            elif option == "2":
                deposit_money()
            elif option == "3":
                withdraw_money()
            elif option == "4":
                view_teansaction_history()
            elif option == "5":
                rate = float(input("Enter annual Interest rate ( as a %):"))
                years = int(input("Enter number of years: "))
                calculate_interest(rate, years)
            elif option == "6":
                conversion_rate = float(input("Enter conversion rate (e.g., 0.85 for Tsh to EUR): "))
                target_currency = input("Enter target currency (e.g., USD): ")
                currency_conversion(conversion_rate, target_currency)
            elif option == "7":
                print("Thank you for using the Pthon banking system. Goodbye!")
                break
            else:
                print("Invalid Option. Please try again")

            #ask user to navigate back
            back_option = input("n\Type 'b' to return to main menu or 'x' to quit: ").lower()
            if back_option == "x":
                print("Thank you for use our Python banking system. Goodnye!")
                break
            elif back_option != 'b':
                print("Invalid input, returning to main menu ....")

#run the Python bank
ussd_menu()