# finding a number using boolean search

list = [1, 2, 3, 4, 5]
found = False

a = int(input("Enter the number to be searched: "))
for i in list:
    if i == a:
        found = True

if found == True:
    print("Number found.")
else:
    print("Number not found.")
