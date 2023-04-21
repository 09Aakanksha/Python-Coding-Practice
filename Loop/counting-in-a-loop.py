# Counting in a loop.

total_count = 0

for i in range(5):
    num = int(input(f"Enter value #{i + 1}:"))
    total_count += 1
print("Number of loops:", total_count)
