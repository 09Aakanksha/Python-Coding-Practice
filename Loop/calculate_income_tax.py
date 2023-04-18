# Exercise 12: Calculate income tax for the given income by adhering to the below rules
# Taxable Income	Rate (in %)
# First $10,000	0
# Next $10,000	10
# The remaining	20
#
# Expected Output:
#
# For example, suppose the taxable income is 45000 the income tax payable is
#
# 10000*0% + 10000*10%  + 25000*20% = $6000.

s = int(input("Input your salary: "))
income_tax = 0
a = 0
if s <= 10000:
    income_tax = 0
    salary = s
    print("Income Tax:", income_tax, "INR")
    print("In hand salary:", salary, "INR")
elif s <= 20000:
    a = s - 10000
    income_tax = (a * 10) / 100
    salary = s - income_tax
    print("Income Tax:", income_tax, "INR")
    print("In nad salary:", salary, "INR")
else:  # 90000
    a = s - 20000  # 70000
    income_tax = (a * 20) / 100 + (10000 * 10) / 100
    salary = s - income_tax
    print("Income Tax:", income_tax, "INR")
    print("In hand salary:", salary, "INR")
