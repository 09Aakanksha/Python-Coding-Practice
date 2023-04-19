# Write a programme to take input number of stings and then append that strings all together with a separator **

num_strings = int(input("Enter the number of strings to append: "))
strings = []

for i in range(num_strings):
    string = input(f"Enter string #{i + 1}: ")
    strings.append(string)

result = "**".join(strings)
print(f"The result is: {result}")
