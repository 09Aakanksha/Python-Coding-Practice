# Exercise 5: Accept a list of 5 float numbers as an input from the user
#
# Refer:
#
#     Take list as a input in Python.
#     Python list
#
# Expected Output:
#
# [78.6, 78.6, 85.3, 1.2, 3.5]
# Show Hint
#
#     Create a list variable named numbers
#     Run loop five times
#     In each iteration of the loop, use the input() function to take input from a user
#     Convert user input to float number using the float() constructor
#     Add float number to the numbers list using the append() function
#
# Show Solution
list = []
for i in range(0, 5):
    a = float(input(f"Enter a number at location {i}: "))
    list.append(a)

print("User List:", list)
