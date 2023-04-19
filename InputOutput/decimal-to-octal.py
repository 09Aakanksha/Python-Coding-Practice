# Exercise 3: Convert Decimal number to octal using print() output formatting
#
# Given:
#

decimal_number = int(input("Enter a Decimal number: "))
octal_number = ''

while decimal_number > 0:
    remainder = decimal_number % 8
    octal_number = str(remainder) + octal_number
    decimal_number = decimal_number // 8

print(f"Octal number: {octal_number}")
