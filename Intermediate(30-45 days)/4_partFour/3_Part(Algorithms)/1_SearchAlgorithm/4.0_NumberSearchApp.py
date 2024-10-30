import random

def generate_sorted_list(size, lower_bound=1, upper_bound=100):
    random_list = random.sample(range(lower_bound, upper_bound), size) # Generate unique numbers
    random_list.sort() # Sort the list for binary search
    return random_list

def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index # target found
    return -1 # target not found

def binary_search(arr, target):
    left, right = 0, len(arr) -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid # Targert found
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1 # Target not found

def main():
    size = int(input("Enter the size of the list: "))
    random_list = generate_sorted_list(size)

    print("Generated sorted list: ", random_list)

    target = int(input("Enter a number to search: "))

    # lianer search 
    print("\n----- Linear Search -------")
    result = linear_search(random_list, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found")

    #binary search
    print("\n---- Binary Search -----")
    result = binary_search(random_list, target)

    if result != -1:
        print(f"Element {target} found at index {result}.")
    else:
        print(f"Element {target} not found")

if __name__ == "__main__":
    main()