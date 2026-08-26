# ========================================
# PYTHON ASSIGNMENT - ALL SOLUTIONS
# ========================================

# ========================================
# TASK 1: Grade Classification
# ========================================
def print_grades(percentage):
    """Print grades based on percentage ranges"""
    if percentage > 90:
        print("Grade A")
    elif 80 < percentage <= 90:
        print("Grade B")
    elif 70 < percentage <= 80:
        print("Grade C")
    else:
        print("Grade D - Fail")


# Task 1 Simple Version (without function)
def task_1_simple():
    print("\n=== TASK 1: Grade Classification ===")
    percentage = float(input("Enter your percentage: "))
    print_grades(percentage)


# ========================================
# TASK 2: Print Numbers 1-100 using Loops
# ========================================
def task_2_for_loop():
    """Print numbers 1-100 using for loop"""
    print("\n=== TASK 2: Numbers 1-100 (For Loop) ===")
    for i in range(1, 101):
        print(i, end=" ")
    print()


def task_2_while_loop():
    """Print numbers 1-100 using while loop"""
    print("\n=== TASK 2: Numbers 1-100 (While Loop) ===")
    i = 1
    while i <= 100:
        print(i, end=" ")
        i += 1
    print()


# ========================================
# TASK 3: Prime Numbers between 1 to 10
# ========================================
def is_prime(n):
    """Check if a number is prime"""
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True


def task_3_prime():
    """Print prime numbers between 1 to 10"""
    print("\n=== TASK 3: Prime Numbers (1-10) ===")
    print("Prime numbers between 1 to 10:")
    for num in range(1, 11):
        if is_prime(num):
            print(num, end=" ")
    print()


# ========================================
# TASK 4: All Tasks using Functions
# ========================================
def task_4_all_functions():
    """Execute all tasks using functions"""
    print("\n=== TASK 4: All Tasks Using Functions ===")
    
    # Task 1 with function
    print("\n--- Task 1: Grade Classification ---")
    percentage = float(input("Enter your percentage: "))
    print_grades(percentage)
    
    # Task 2 with functions
    print("\n--- Task 2: Numbers 1-100 ---")
    task_2_for_loop()
    task_2_while_loop()
    
    # Task 3 with function
    print("\n--- Task 3: Prime Numbers ---")
    task_3_prime()


# ========================================
# TASK 7: Linear Search
# ========================================
def linear_search(arr, target):
    """Linear search function - searches through array sequentially"""
    for i in range(len(arr)):
        if arr[i] == target:
            return True
    return False


def task_7_linear_search():
    """Task 7: Linear search implementation"""
    print("\n=== TASK 7: Linear Search ===")
    numbers = [33, 60, 7, 40, 90, 1, 5, 70, 44, 49, 9, 16, 13, 74]
    print(f"Array: {numbers}")
    
    search_value = int(input("Enter a number to search: "))
    
    if linear_search(numbers, search_value):
        print("Found")
    else:
        print("Not found")


# ========================================
# TASK 8: Binary Search
# ========================================
def binary_search(arr, target):
    """Binary search function - searches sorted array using divide and conquer"""
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


def task_8_binary_search():
    """Task 8: Binary search implementation"""
    print("\n=== TASK 8: Binary Search ===")
    # Array with numbers in ascending order
    numbers = [1, 5, 7, 9, 13, 16, 33, 40, 44, 49, 60, 70, 74, 90]
    print(f"Sorted Array: {numbers}")
    
    search_value = int(input("Enter a number to search: "))
    
    if binary_search(numbers, search_value):
        print("Found")
    else:
        print("Not found")


# ========================================
# MAIN MENU
# ========================================
if __name__ == "__main__":
    while True:
        print("\n" + "="*50)
        print("PYTHON ASSIGNMENT - SELECT A TASK")
        print("="*50)
        print("1. Task 1: Grade Classification")
        print("2. Task 2: Numbers 1-100 (For Loop)")
        print("3. Task 2: Numbers 1-100 (While Loop)")
        print("4. Task 3: Prime Numbers (1-10)")
        print("5. Task 4: All Tasks Using Functions")
        print("6. Task 7: Linear Search")
        print("7. Task 8: Binary Search")
        print("8. Exit")
        
        choice = input("\nEnter your choice (1-8): ")
        
        if choice == "1":
            task_1_simple()
        elif choice == "2":
            task_2_for_loop()
        elif choice == "3":
            task_2_while_loop()
        elif choice == "4":
            task_3_prime()
        elif choice == "5":
            task_4_all_functions()
        elif choice == "6":
            task_7_linear_search()
        elif choice == "7":
            task_8_binary_search()
        elif choice == "8":
            print("\nThank you for using the assignment solver!")
            break
        else:
            print("\nInvalid choice! Please try again.")
