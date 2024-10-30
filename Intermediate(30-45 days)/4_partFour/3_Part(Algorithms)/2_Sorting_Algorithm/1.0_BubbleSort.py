def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j +1]:
                arr[j], arr[j+1] = arr[j+1], arr[j] #swap
    return arr

# Usage
unsorted_list = [64, 34, 25, 12, 22, 11, 90]
sorted_list = bubble_sort(unsorted_list)
print("sorted list (Bubble Sort): ", sorted_list)