# Exercise 5: Check if the first and last number of a list is the same
#
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.
#
# Given:
#
# numbers_x = [10, 20, 30, 40, 10]
# numbers_y = [75, 65, 35, 75, 30]
#
# Expected Output:
#
# Given list: [10, 20, 30, 40, 10]
# result is True
#
# numbers_y = [75, 65, 35, 75, 30]
# result is False

list = [1, 2, 3, 2, 2]
n = len(list)

if list[0] == list[n - 1]:
    print("Result is True.")
else:
    print("Result is False.")
