def calcaulate_total():
    prices = [] #list
    while True:
        price = input("Enter the price of the item ( or type 'done' to finish): ")
        if price.lower() == 'done':
            break
        try:
            prices.append(float(price))
        except ValueError:
            print("Invalid input, please enter valid amount")

    total = sum(prices)
    print(f"Total amount: Tsh {total:.2f}")

calcaulate_total()