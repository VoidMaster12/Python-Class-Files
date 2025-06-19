#Function-drills.py
#Matthew Raines, COP2500

#Imports turtle, random, and math libraries

import math
import turtle
import random

'''A function comment should include:

*The function's name.
*What the function does.
*What each parameter does.
*What, if anything, gets returned.
*What can go wrong.'''

#floatinator: Promps the user with the provided string, accepts an input from
#the user and returns the input forced into a floating-point number. Causes an
#error if the user doesn't type a float.

def floatinator(prompt):
    z=float(input(prompt))
    return z

#z=floatinator("Enter a number: ")      This would call the function.

#Math library has its own functions, such as sqrt()

print (math.pi)
print(math.sqrt(4))
print("") #Puts a blank line in between this and the function results

#EXERCISE ---

#circle_area: Calculates the area of a circle given the radius. It returns the
#area. Causes an error if the radius isn't a number.

def circle_area(radius):
    area=math.pi*(radius)**2
    return area

#area=circle_area(4)        Calls the function

#EXERCISE ---

#tri_hyp: Returns the length of the hypoteneuse of a right triangle given the
#opposite and adjacent side lengths. Causes an error if either side length is
#not a number.

def tri_hyp(adj,opp):
    hyp=math.sqrt(adj**2 + opp**2)
    return hyp

#hyp=tri_hyp(3,4)       Calls the function

#EXERCISE ---

#turtle_mobilizer: Accepts a turtle and x,y coordinate, and moves the turtle to
#the x,y coordinate without drawing anything. Returns nothing. Causes an error
#if the coordinates aren't numbers, or if it isn't given a tur (turtle).

def turtle_mobilizer(tur,x,y):
    tur.penup()
    tur.goto(x,y)
    tur.pendown()

'''screen=turtle.getscreen()
screen.bgcolor("cyan")
tur=turtle.Turtle()

turtle_mobilizer(tur,-200,-100)'''

#EXERCISE ---

#tri_area: Returns the area of a right triangle given its opposite and adjacent
#lengths. Causes an error if the adjacent or opposite length isn't a number.

def tri_area(opp,adj):
    area=0.5*opp*adj
    return area

# EXERCISE ---

#cylinder_vol: Returns the volume of a cylinder given its radius and height.
#Causes an error if the radius or height isn't a number.

def cylinder_vol(radius,height):
    vol=math.pi*(radius**2)*height
    return vol

# EXERCISE ---

#cylinder_vol: Returns the volume of a cylinder given its radius and height.
#Causes an error if the radius or height isn't a number.

def cyl_vol(radius,height):
    area=circle_area(radius)
    volume=height*area
    return volume

#EXERCISE ---

#tur_spin: Given a turtle, x, and y coordinate, moves the turtle to the x,y
#coordinate and spins the turtle. Returns nothing. Causes an error if x or y is
#not a number, or if it isn't given a turtle as the first parameter.

def tur_spin(t,x,y):
    turtle_mobilizer(t,x,y)
    t.rt(720)

#EXERCISE ---

#random_tp: Given a turtle, generates a random x and y coord from -100,100 and
#teleports the turtle there without drawing anything, then spins it twice.
#Returns nothing. Causes an error if it isn't given a turtle in the parameters.

def random_tp(t):
    x=random.randint(-100,100)
    y=random.randint(-100,100)
    tur_spin(t,x,y)

#EXERCISE---

#sigma_i: Given an n, summates the number from i to n. Returns the summation.
#Causes an error if n isn't a number.

def sigma_i(n):
    summation=0
    for i in range (1,n+1):
        summation=summation+i
    return summation
