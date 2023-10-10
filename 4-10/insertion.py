def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

# Example usage:
arr = [64, 25, 12, 22, 11]
insertion_sort(arr)
print("Sorted array:", arr)

def insertion_sort(nums):
    """
    Sorts a list of integers using the Insertion Sort algorithm.
    
    Args:
    nums (list of int): The list of integers to be sorted.
    
    Returns:
    list of int: The sorted list.
    """
    n = len(nums)
    
    # Traverse through all elements in the list
    for i in range(1, n):
        key = nums[i]  # Current element to be compared
        
        # Move elements of nums[0..i-1] that are greater than key
        # to one position ahead of their current position
        j = i - 1
        while j >= 0 and key < nums[j]:
            nums[j + 1] = nums[j]
            j -= 1
        nums[j + 1] = key
    
    return nums

# Sample Input
input_list = [5, 2, 9, 1, 5]

# Sorting the list using insertion_sort
sorted_list = insertion_sort(input_list)

# Printing the sorted list
print("->".join(map(str, sorted_list)))
