# Raising Exceptions
age = int(input("Enter your age: "))
if age < 0 :
    raise ValueError("Age cannot be negative!")
else:
    print(f"You age is {age}.")