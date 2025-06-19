#Draw_triangle.py
#Matthew Raines, COP 2500

#Draws a triangle using turtle given hypoteneuse and one angle as input.

#Gets turtle and math

import turtle
import math

#get_float: Given a string prompt, asks the user for input using the prompt and
#converts it into a float. Returns the float number. Causes an error if the user
#doesn't enter a number.

def get_float(prompt):
    result=float(input(prompt))
    return result

#Find_opp: Given the hypoteneuse and one angle, returns the opposite side
#length. Causes an error if hypoteneuse or angle isn't a number, or if the angle
#isn't given in degrees.

def Find_opp(hyp,angle):
    opp=hyp*math.sin(angle)
    return opp

#Find_opp: Given the hypoteneuse and adj side, returns the opposite side
#length. Causes an error if hypoteneuse or adj isn't a number.

def Find_adj(hyp,opp):
    adj=math.sqrt(hyp**2 - opp**2)
    return adj

#draw_triangle: Draws a right triangle gives the hyp, opp, adj, and one angle.
#Returns nothing. Causes an error if the angle is in radians or if any value is
#not a number.

def draw_triangle(hyp,opp,adj,angle):
    turtle.fd(adj)
    turtle.lt(90)
    turtle.fd(opp)
    turtle.lt(90+angle)
    turtle.fd(hyp)


#Main Program Begins Here-----

#Gets the hypotenuse and angle

hyp=get_float("Enter Hypoteneuse Length: ")
theta=get_float("Enter Angle (in degrees): ")

#Calculates the side lengths and other angles

thetaRad=math.radians(theta)
opp=Find_opp(hyp, thetaRad)
adj=Find_adj(hyp, opp)

#Draws the triangle

draw_triangle(hyp,opp,adj,theta)
