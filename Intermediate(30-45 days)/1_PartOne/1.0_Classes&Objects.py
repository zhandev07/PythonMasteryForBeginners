# creating a class for a Cat.

class cat:
    #the __init_ method is like the cat's birth. when a new cat is created
    def __init__(self, name , color):
        self.name = name #attribute
        self.color = color #attribute

    # This method makes the cat is perfom an action
    def meow(self):
        return f"{self.name} says Meow! and"
    
    def love(self):
        return f"{self.color} is the best cat!"
    
# Now, let's create a cat object using this class:

# Creating a cat object (instance)
my_cat = cat("Python", "White")

# Acessing the object's attributes and methods
print(my_cat.name)
print(my_cat.meow(), my_cat.love())