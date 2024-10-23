import os
#define the addition 
def add(x, y):
    return x + y

#sub
def sub(x, y):
    return x + y

#mulp
def mult(x, y):
    return x + y

#div
def div(x, y):
    try:
        return x/y
    except ZeroDivisionError:
        return "Error! Cannot divide by zero"

__path__ = r"C:/Users/lucian/Desktop/python/Beginner(7-14days)/projects_for_beginers/ToDoListApp/caclulate_history.txt"

#load history to file
def load_history():
    if os.path.exists(__path__):
        with open(__path__, 'r') as file:
            return file.readlines()
    return[]

#save history to file
def save_history(history):
    with open(__path__, "w") as file:
        for record in history:
            file.write(record + "\n")


#function to diplay the calculator menu

def display_menu():
    print("\n Python Calculator")
    print("Select Operation:")
    print("1. add")
    print("2. subtract")
    print("3. multiply")
    print("4. Divide")
    print("5. View History")
    print("6. clear History")
    print("7. Quit")


#functon to handle user input
def calculator():
    history = load_history()
    while True:
        display_menu()
        choice = input("Enter a choice (eg 1,2,3,4,5,6,7): ")

        if choice in ['1', '2', '3', '4']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second Number: "))
            except ValueError:
                print("Invalid input! Please enter numbers only.")
                continue

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}" 
            elif choice == '2':
                result = sub(num1, num2)
                operation = f"{num1} + {num2} = {result}" 
            elif choice == '3':
               result = mult(num1, num2)
               operation = f"{num1} + {num2} = {result}" 
            elif choice == '4':
                result = div(num1, num2)
                operation = f"{num1} + {num2} = {result}" 
            
            print(operation)
            history.append(operation) #store history
            save_history(history)

        elif choice == '5':
            if not history:
                print("\n No Calculator history yet")
            else:
                print("\n Calculation History: ")
                for record in history:
                    print(record.strip())
                    
        elif choice == '6':
            history.clear()
            save_history(history) #clear the file too
            print("history cleared.")
        
        elif choice == '7':
            print("Goodbye!")
            break

        else:
            print("Invalid choice! Please select a valid option!")
#run 
calculator()