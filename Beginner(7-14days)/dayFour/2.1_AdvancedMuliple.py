# Calculating Total Price

def calculate_total_price(item_prices):
    total = sum(item_prices)
    return total

#List of price for a customer
customer_prices = [2000.00, 10000.00, 30000.00]
total_price = calculate_total_price(customer_prices)

print(f"Total price : Tsh {total_price:.2f}")



# Combining Functions with Loops
customers = ["Python", "php", "Java"]

def my_customers(name):
    print(f"Hello, {name} how are you today!")

for customer in customers:
    my_customers(customer)

