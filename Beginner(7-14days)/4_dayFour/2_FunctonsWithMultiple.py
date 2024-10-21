#functions to add a two numbers

#define the functions
def add_numbers(a, b):
    result = a + b
    print(f"The sum of {a} and {b} is {result}")

#call the functions
# without user input
add_numbers(10, 12)


# ask user to input the number
a = int(input("Enter a first number: "))
b = int(input("Enter a second number: "))

add_numbers(a, b)


# 2 Returning Values from a Function

def sub_numbers(x,y):
    return x - y 

#store the result in a varable
Total = sub_numbers(12, 10)
print(Total)