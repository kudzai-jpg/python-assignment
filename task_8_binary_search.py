# Task 8: Binary Search

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return False

# Array with numbers in ascending order
numbers = [1, 5, 7, 9, 13, 16, 33, 40, 44, 49, 60, 70, 74, 90]

# Search for a value
search_value = int(input("Enter a number to search: "))

if binary_search(numbers, search_value):
    print("Found")
else:
    print("Not found")
