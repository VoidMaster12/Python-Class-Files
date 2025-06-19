# Matt

# Conditionals

'''
    if {condition}:
        do this
    else:
        do something else
'''

# Since 10 > 5, the if block runs and the else block doesnt
if 10 > 5:
    print("10 is greater!")
else:
    print("The code broke")

# Since 10 < 5 is false, the else block runs and the if block doesnt
if 10 < 5:
    print("10 is less!")
else:
    print("The code works")

x = int(input("Enter the x: "))
y = int(input("Enter the y: "))

# Different conditions
'''
if x > y    greater than
if x < y    less than
if x >= y   greater than or equal to
if x <= y   less than or equal to
if x == y   equal to
if x != y   not equal to
'''

if x > y:
    print("1")
elif x < y:
    print("2")
elif x == y:
    print("3")
else:
    print("oops")

name = "bob"

if name == "bob":
    print("bob!")


# Write a program that gets 2 numbers from the user, takes the largest of the 2 numbers and prints whether or not
# the largest of the 2 numbers is greater than or less than the smaller number times 1.5

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

if num1 > num2:
    larger_num = num1
    smaller_num = num2
elif num1 < num2:
    larger_num = num2
    smaller_num = num1
else:
    larger_num = num1
    smaller_num = num2

if larger_num > smaller_num * 1.5:
    print(f"The larger number {larger_num} is over 1.5 times greater than the smaller number {smaller_num}!")
elif larger_num <= smaller_num * 1.5:
    print(f"The larger number {larger_num} is not 1.5 times greater than the smaller number {smaller_num}.")