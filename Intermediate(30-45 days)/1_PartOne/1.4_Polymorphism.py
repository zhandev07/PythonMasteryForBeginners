# For example, both Dog and Cat have a make_sound() method, but they behave differently (bark vs meow).
#parent class
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound"
    
# child class that inherits form animal parent class
class Dog(Animal):
    def make_sound(self):
        return f"{self.name} barks!"

# Anothe class thas inherit from animal parent class
class Cat(Animal):
    def make_sound(self):
        return f"{self.name} Meows!"
    
# creating objects
dog = Dog("Python")
cat = Cat("Toni")

print(dog.make_sound())
print(cat.make_sound())