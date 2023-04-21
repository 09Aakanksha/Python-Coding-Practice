# finding a number using boolean search

list = [1, 2, 3, 4, 5]
found = False

for i in list:
    if i == 6:
        found = True

if found == True:
    print("Number found.")
else:
    print("Number not found.")
