# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
#
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

n = int(input("Enter any number: "))
original = n

while n > 0:
    remainder = n % 10
    n = n // 10
    print(remainder, end=" ")
