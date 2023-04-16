s = input("Enter a string: ")
n = len(s)
output = ""

for i in range(n - 1, -1, -1):
    output = output + s[i]

print(output)

