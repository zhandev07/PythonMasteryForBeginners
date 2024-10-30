# Interpolation Search
def Interpolation_Search(arr, target):
    low, high = 0, len(arr) -1

    while low <= high and target >= arr[low] and target <= arr[high]:
        if low == high:
            if arr[low] == target:
                return low
            return -1
        
        # 3 Estimate the position
        pos = low + ((target - arr[low]) * (high - low) // (arr[high] - arr[low]))


        if arr[pos] == target:
            return pos
        if arr[pos]  < target:
            low = pos + 1
        else:
            high = pos -1

    return -1

# Usage
uniform_sorted_numbers = [10, 20, 30, 40, 50]
target = 40
result = Interpolation_Search(uniform_sorted_numbers, target)

if result != -1:
    print(f"ELement {target} found at index {result}.")
else:
    print(f"ELement {target} not found")