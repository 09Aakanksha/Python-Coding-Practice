for i in range(1, 101):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + " Fizz Buzz")
    elif i % 3 == 0:
        print(str(i) + " Fizz")
    elif i % 5 == 0:
        print(str(i) + " Buzz")
    else:
        print(str(i) + " Neither divisible by 3 nor 5")
