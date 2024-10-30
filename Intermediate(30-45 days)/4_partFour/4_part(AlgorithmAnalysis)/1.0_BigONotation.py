# Example 1: Constant Time O(1)

def get_first_element(lst):
    return lst[0]  # O(1) - accessing the first element is constant time

# Example 2: Linear Time O(n)

def print_all_elements(lst):
    for element in lst:
        print(element)  # O(n) - must iterate through the entire list

# Example 3: Quadratic Time O(n²)
def print_pairs(lst):
    for i in range(len(lst)):
        for j in range(len(lst)):
            print(lst[i], lst[j])  # O(n²) - nested loops


#  Example of Time and Space Complexity

def sum_of_elements(lst):
    total = 0          # O(1) space
    for element in lst:  # O(n) time
        total += element  # O(1) for addition
    return total
# Overall: Time complexity = O(n), Space complexity = O(1)
