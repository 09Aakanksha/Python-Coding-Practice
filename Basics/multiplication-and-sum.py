# Given two integer numbers return their product only if the product is equal to or lower
# than 1000, else return their sum.
#
# Given 1:
#
# number1 = 20
# number2 = 30
#
# Expected Output:
#
# The result is 600
#
# Given 2:
#
# number1 = 40
# number2 = 30
#
# Expected Output:
#
# The result is 70
# if a * b <= 1000:
#     print(a * b)
# else:
#     print(a + b)

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

product = a * b
sum = a + b

if product <= 1000:
    print(product)
else:
    print(sum)
