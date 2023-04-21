# finding the largest value:

largest_num_so_far = 0

for num in range(5):
    n = int(input(f"Enter number #{num + 1}:"))
    if n > largest_num_so_far:
        largest_num_so_far = n

print(largest_num_so_far)
