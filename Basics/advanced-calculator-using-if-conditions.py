# ADVANCED CALCULATOR

num1 = float(input("Enter first number: "))
op = input("Enter an operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)

elif op == "-":
    print(num1 - num2)

elif op == "*":
    print(num1 * num2)

elif op == "/":
    if num2 == 0:
        print("You are not allowed to devide by ZERO")
    else:
        print(num1 / num2)

elif op == '%':
    print(num1 % num2)

else:
    print("ERROR: You have entered a wrong operator.")
