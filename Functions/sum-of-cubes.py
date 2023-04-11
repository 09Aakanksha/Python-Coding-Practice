def calculateCube(num):
    value = num * num * num
    return value


def calculateSum(a, b, c):
    cubeOfA = calculateCube(a)
    cubeOfB = calculateCube(b)
    cubeOfC = calculateCube(c)

    sum = cubeOfA + cubeOfB + cubeOfC
    return sum


a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

print(calculateSum(a, b, c))
