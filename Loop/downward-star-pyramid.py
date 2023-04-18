# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
#
# * * * * *
# * * * *
# * * *
# * *
# *

n = int(input("Enter a number: "))

for i in range(n, 0, -1):
    for j in range(0, i):
        print("*", end=" ")
    print()
