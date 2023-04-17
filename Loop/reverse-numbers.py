n = int(input("Enter a number: "))
original = n
reverse = 0

while n > 0:
    remainder = n % 10
    n = n // 10
    reverse = reverse * 10 + remainder

print("Original number was", original, "! Reverse of this number is", reverse, ".")
