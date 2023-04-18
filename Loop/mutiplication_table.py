# Exercise 13: Print multiplication table form 1 to 10


n = int(input("Enter a number: "))
for i in range(1, n + 1):
    print(i, end="\t")
    for j in range(2, 11):
        print(i * j, end=" ")
    print()
