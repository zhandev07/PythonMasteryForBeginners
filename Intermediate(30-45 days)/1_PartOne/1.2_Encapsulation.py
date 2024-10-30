# Encapsulated(private)
class CoffeeMachine:
    def __init__(self, water_level):
        self.__water_level = water_level # Encapsulated (private) attribute

    def make_coffee(self):
        if self.__water_level > 0:
            self.__water_level -=1
            return "Here's your coffee!"
        else:
            return "Not enought water"
        
#use the machine coffee
machine = CoffeeMachine(3)
print(machine.make_coffee())# Output: Here's your coffee!
print(machine.make_coffee())# Output: Here's your coffee!
print(machine.make_coffee())# Output: Here's your coffee!
print(machine.make_coffee())# Output: Not enought water!