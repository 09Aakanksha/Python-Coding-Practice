# Exercise 5: Check if the last number of two lists are the same.
#

x = [1, 2, 3, 4, 6, 9]
y = [1, 3, 6, 4, 5]

n = len(x)
m = len(y)

if x[n - 1] == y[m - 1]:
    print("True")
else:
    print("False")
