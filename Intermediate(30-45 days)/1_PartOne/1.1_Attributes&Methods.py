class phone:
    def __init__(self, brand, color, storage):
        self.brand = brand
        self.color = color
        self.storage = storage

    def call(self, number):
        return f"Calling {number} using {self.brand} phone....."
    
#create a phone object
my_phone = phone("Samsung", "Titanium black", "64GB")
print(my_phone.call("+255111111111"))