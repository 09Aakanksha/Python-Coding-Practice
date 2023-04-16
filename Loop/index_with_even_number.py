# Exercise 3: Print characters from a string that are present at an even index number
#
# Write a program to accept a string from the user and display characters that are present at an even index number.
#
# For example, str = "pynative" so you should display ‘p’, ‘n’, ‘t’, ‘v’.
#
# Expected Output:
#
# Orginal String is  pynative
# Printing only even index chars
# p
# n
# t
# v

str = input("Enter a string: ")
n = len(str)
for i in range(0, n, 2):
    print(str[i], i)
