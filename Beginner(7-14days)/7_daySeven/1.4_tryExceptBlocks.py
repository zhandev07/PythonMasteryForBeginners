# Using Try and Except Blocks
try:
    numerator = float(input("Enter numerator: "))
    denominator = float(input("Enter denominator: "))
    result = numerator / denominator

    print(f"The results is: {result}")
except ZeroDivisionError:
    print("Oops! You can't divide by zero.")
except ValueError:
    print("Invalid input! Please enter a number.")