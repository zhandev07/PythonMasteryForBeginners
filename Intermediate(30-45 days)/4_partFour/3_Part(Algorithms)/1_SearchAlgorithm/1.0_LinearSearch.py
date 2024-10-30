def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index # Target found, return index
    return -1  # Target not found

# usage
numbers = [10, 20, 30, 40, 50]
target = 30
result = linear_search(numbers, target)

if result != -1:
    print(f"Element {target} found at index {result}.")
else:
    print(f"Element {target} not found")