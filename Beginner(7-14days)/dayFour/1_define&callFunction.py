#simple functions 

#define the functin first eg say _hello is our fuctions
def say_hello(name):
    print(f"Hello, {name}!")

#call the funstions

say_hello("Python")
say_hello("Php")
say_hello("Java")


#more complex example use combile loop on day 3 with function
number_names = int(input("Enter a total numbers of names!: "))

names = []

for i in range(number_names):
    name = input(f"Enter a name #{i+1}: ")
    names.append(name)

def greating_people(name):
    print(f"Hello! your names is {name} nice to meet you!")

for name in names:
    greating_people(name)