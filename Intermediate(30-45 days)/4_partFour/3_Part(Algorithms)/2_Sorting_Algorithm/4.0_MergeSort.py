def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left_half = arr[:mid]
        right_half = arr[mid:]

        merge_sort(left_half)  # Sort the left half
        merge_sort(right_half)  # Sort the right half

        i = j = k = 0  # Initial indexes for left, right, and merged array

        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

    return arr

# Example Usage
unsorted_list = [38, 27, 43, 3, 9, 82, 10]
sorted_list = merge_sort(unsorted_list)
print("Sorted list (Merge Sort):", sorted_list)
