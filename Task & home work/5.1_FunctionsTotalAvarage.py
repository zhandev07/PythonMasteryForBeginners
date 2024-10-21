# 3. Shopping Cart (Total and Average Price)
def shopping_cart(prices):
    Total = sum (prices) #sum of all price
    avarage = Total / len(prices)
    return Total, avarage

#let use and call the function now
item_price = [20000, 20000, 50000, 30000]
Total, avarage = shopping_cart(item_price)

print(f"Total: Tsh {Total:.2f}, Avarage price: Tsh{avarage:.2f}")