
#Functions with Default Values
#Default Discount
def calculate_discount(price, discount=0.1):
    final_price = price - (price * discount)
    return final_price

# Use the deafault discount(10%)
print(calculate_discount(100))

#Specify a custom discount (20%)
print(calculate_discount(100, 0.2))


# Repeatedly Calculate Discounts with Loops
my_prices = ["1000.00", "5000.00", "60000.00", "100000.00"] #not you not allow to use string so correct is [1000.00, 5000.00, 60000.00, 100000.00]


for price in my_prices:
    price = float(price) #convert to string to float
    tot_price = calculate_discount(price, 0.3)
    print(f"Original Price: Tsh{price:.2f}, after discount: Tsh {tot_price:.2f}")