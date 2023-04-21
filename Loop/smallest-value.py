# finding the smallest value:

smallest_so_far = float('inf')

for i in range(5):
    a = int(input(f"Enter number#{i + 1}:"))
    if a < smallest_so_far:
        smallest_so_far = a
print("Smallest value:", smallest_so_far)

# 5 4 3 2 1
