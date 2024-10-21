balance = 0

def check_balance():
    print(f"your balance is Tsh {balance:.2f}")

def deposit_money(amount):
    global balance  # Allows us to modify the global balance variable
    balance += amount
    print(f"Tsh{amount:.2f} deposited. New balance: Tsh{balance:.2f}")

def withdraw_money(amount):
    global balance
    if amount > balance :
        print("Insufficent balance!")
    else:
        balance -= amount
        print(f"TSh{amount} withdrawn. New balance remaining : Tsh {balance:.2f}")

# usage of those function
while True:
    action = input("Enter 'check, 'deposit', 'withdraw', or 'exit': ").lower()


    if action == 'check':
        check_balance()
    elif action == 'deposit':
        amount = float(input("Enter the deposit amount: "))
        deposit_money(amount)
    elif action == 'withdraw':
        amount = float(input("Enter the withdraw amout: "))
        withdraw_money(amount)
    elif action == 'exit':
        print("Exit banking system")
        break
    else:
        print("Invalid action! please try again.!")