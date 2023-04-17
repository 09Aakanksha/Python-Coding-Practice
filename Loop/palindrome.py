# Write a program to check if the given number is a palindrome number.
#
# A palindrome number is a number that is same after reverse. For example 545, is the palindrome numbers
#
# Expected Output:
#
# original number 121
# Yes. given number is palindrome number
#
# original number 125
# No. given number is not palindrome number
# Considering number as string
s = input("Enter a number: ")
n = len(s)
output = ""

print("Original number: ", s)
for i in range(n - 1, -1, -1):
    output = output + s[i]

if s == output:
    print(output, "is palindrome.")
else:
    print(output, "is not a palindrome number.")

# considering number as integer.

n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    remainder = n % 10
    n = n // 10
    reverse = reverse * 10 + remainder

print("Original number was", original, "! Reverse of this number is", reverse, ".")
