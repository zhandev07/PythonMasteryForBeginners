# 2. Simple Calculator Use functions and conditions
def calculator(num1, num2, operator):
    if operator == "+":
        return num1 + num2 
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error! Division by zero"
        return num1/num2
    else:
        return "Invalid operator!"
    
#ask user to input the number
num1 = int(input("Enter the first number?:"))
operator = input("Enter the Operator eg +,-,*,/?:")
num2 = int(input("Enter the second number?:")) 

result = calculator(num1, num2, operator)

print(result)