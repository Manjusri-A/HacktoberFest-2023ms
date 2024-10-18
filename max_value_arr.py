# Approach 1: Sorting the initial list and returning the last element
def max_element_sort(arr):
    arr.sort()
    return arr[-1]

# Approach 2: Iterating through all the elements in the list and comparing each element
def max_element_iter(arr):
    max_element = arr[0]
    for i in range(1, len(arr)):  # Start from index 1
        if arr[i] > max_element:
            max_element = arr[i]
    return max_element

# Approach 3: Using the built-in function
def max_element_builtin(arr):
    return max(arr)  # Use built-in max

# Example usage
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
print("Max using sort:", max_element_sort(numbers.copy()))
print("Max using iteration:", max_element_iter(numbers.copy()))
print("Max using built-in function:", max_element_builtin(numbers.copy()))
