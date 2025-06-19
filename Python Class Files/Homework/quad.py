#quad.py - Quadratic root finder
#Matthew Raines, COP2500

#This was written to determine the number of roots a quadratic equation has.
#This may be able to help me with my calc II homework as well.

#Imports the math library

import math

#root_value: Given the a,b,c value of a quadratic, returns the value of the
#number under the radical (b^2-4ac). It returns the value under the root. Causes
#an error if a, b, or c are not numbers.

def root_value (a,b,c):
    root=b**2 - 4*a*c
    return root

#root_one: Given a, b and the value of the number under the radical, returns the
#first root where the root is added. An error occurs if the number under the
#root is negative, or if a or b is not a number.

def root_one (a,b,root):
    first_root=(-b + math.sqrt(root))/(2*a)
    return first_root

#root_two: Given a, b and the value of the number under the radical, returns the
#second root where the root is subtracted. An error occurs if the number under
#the root is negative, or if a or b is not a number.

def root_two (a,b,root):
    second_root=(-b - math.sqrt(root))/(2*a)
    return second_root             


# SMain Program Begins Here-----

#Gets the a, b, c value from the user.

a=float(input("Enter the value for coefficient a: "))
b=float(input("Enter the value for coefficient b: "))
c=float(input("Enter the value for coefficient c: "))

#Calculates the value under the square root.

rad = root_value(a,b,c)

#Checks if the value under the root is negative or 0. If negative, there's no
#roots. If 0, there is only one root. It then calculates the root's value and
#prints it. If it's greater than 0, it calculates both roots and prints them.

if rad < 0:
    print("There are no real roots!")
elif rad == 0:
    first_root=root_one(a,b,rad)
    print("There is one root for that quadratic:",first_root)
else:
    first_root=root_one(a,b,rad)
    second_root=root_two(a,b,rad)
    print("The two roots for that quadratic are:",first_root,"and",second_root)

