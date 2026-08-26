# Task 1: Grade Classification Program
# Print grades based on percentage ranges

percentage = float(input("Enter your percentage: "))

if percentage > 90:
    print("Grade A")
elif 80 < percentage <= 90:
    print("Grade B")
elif 70 < percentage <= 80:
    print("Grade C")
else:
    print("Grade D - Fail")
