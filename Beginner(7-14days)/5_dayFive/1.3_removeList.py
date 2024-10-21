# 3 Accessing Items in a  List for movie night
snacks = ["popcorn", "chips", "soda", "candy"]

#remove 'chips'
# Using remove(): This method removes the first occurrence of a value:
snacks.remove("chips")
print(snacks)


# or use Using pop(): This removes the item at a specific index and returns it:
last_item = snacks.pop()
print(last_item)
print(snacks)

#or Using del: This can remove an item or the entire list:
del snacks[0] #delecte popcorn
print(snacks)