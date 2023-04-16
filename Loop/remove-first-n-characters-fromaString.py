# Exercise 4: Remove first n characters from a string
#
# Write a program to remove characters from a string starting from zero up to n and return a new string.
#
# For example:
#
#     remove_chars("pynative", 4) so output must be tive. Here we need to remove first four characters from a string.
#     remove_chars("pynative", 2) so output must be native. Here we need to remove first two characters from a string.
#
# Note: n must be less than the length of the string.

s = input("Enter a string: ")
length = len(s)
n = int(input("Enter the number of characters, you want to remove from the start of string: "))
# Variable to store output
output = ""

if length < n:
    print("Invalid value - n cannot be greater than length of the string.")
else:
    for i in range(n, length):
        output = output + s[i]

print(output)
