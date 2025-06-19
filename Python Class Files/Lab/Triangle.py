#Triangle.py

import math

#root= math.sqrt(4)
#root=4**(.5)
#print(root)

#Raising a number to the .5 or 1/2 power is the same as taking the sqrt

opp= float(input("Enter opposite side length:\n"))
adj= float(input("Enter adjacent side length:\n"))

'''The \n makes the input go to a new line. It's just for formatting. That works
for all commands even print statements'''

#Calculating the Hypotenuse.
hyp=math.sqrt(opp**2+adj**2)
print("The side lengths are",opp,adj,hyp)

#Calculating the Perimeter.
perim=opp+adj+hyp
print("Perimeter =",perim)

angle=math.asin(opp/hyp)
print("Angle (Radians) =",angle)
print("Angle (Degrees) =", math.degrees(angle))

#The math.degrees puts the angle in degrees, as the math function works in
#radians by default.
