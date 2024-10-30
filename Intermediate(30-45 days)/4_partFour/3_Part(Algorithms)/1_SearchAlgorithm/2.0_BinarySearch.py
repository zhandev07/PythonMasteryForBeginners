def binary_search(arr, target):
    lelf, right  = 0, len(arr) -1

    while lelf <= right:
        mid = (lelf + right) // 2 # Find the middle index
        if arr[mid] == target:
            return mid # Target found
        elif arr[mid] < target:
            lelf = mid + 1 # search in the right half
        else:
            right = mid -1 # Search in the left half

    return -1 #target not found

# Usage
sorted_numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
target = 60
result = binary_search(sorted_numbers, target)

if result != -1:
    print(f"Element {target} found at Index {result}.")
else:
    print(f"Elements {target} not found")