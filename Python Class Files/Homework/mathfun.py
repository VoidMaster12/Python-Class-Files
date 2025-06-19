#mathfun.py - Using fun trig calculations
#Matthew Raines, COP2500

#This was written to do trig calculations to find the sides and angles of a
#right triangle, which is hopefully easier than my calc hw I just did.

#Imports the math library.

import math

#adj_length: Given the hypotenuse length and adjacent angle, calculates and
#returns the adjacent length. Causes an error if the hypotenuse or angle isn't
#a number, or if the angle isn't given in degrees.

def adj_length(hyp,adj_angle):
    rad_adj_angle=math.radians(adj_angle)
    adj=hyp*math.cos(rad_adj_angle)
    return adj

#opp_length: Given the hypotenuse length and adjacent angle, calculates and
#returns the opposite length. Causes an error if the hypotenuse or angle isn't
#a number, or if the angle isn't given in degrees.

def opp_length(hyp, adj_angle):
    rad_adj_angle=math.radians(adj_angle)
    opp=hyp*math.sin(rad_adj_angle)
    return opp

#find_adj_angle: Given the hypotenuse and opposite length, calculates and
#returns the adjacent angle. Causes an error if the hypotenuse or opposite
#isn't a number.

def find_adj_angle(hyp,opp):
    adj_angle=math.asin(opp/hyp)
    deg_adj_angle=math.degrees(adj_angle)
    return deg_adj_angle

#find_adj_angle_again: Given the adjacent and opposite length, calculates and
#returns the  adjacent angle. Causes an error if the adjacent or opposite isn't
#a number.

def find_adj_angle_again(opp,adj):
    adj_angle_two=math.atan(opp/adj)
    deg_adj_angle_two=math.degrees(adj_angle_two)
    return deg_adj_angle_two

#----Main Program----

#Gets the input from the user.

adj=float(input("Enter the adjacent length: "))
opp=float(input("Enter the opposite length: "))
hyp=float(input("Enter the hypotenuse length: "))
adj_angle=float(input("Enter the adjacent angle in degrees: "))

#Calculates the side lengths and adjacent angle using functions and prints them.

new_adj=adj_length(hyp, adj_angle)
print("The adjacent length is:",new_adj)

new_opp=opp_length(hyp,adj_angle)
print("The opposite length is:",new_opp)

new_adj_angle=find_adj_angle(hyp,opp)
print("The adjacent angle, in degrees, is:",new_adj_angle)

new_new_adj_angle=find_adj_angle_again(opp,adj)
print("If the adjacent angle isn't",new_new_adj_angle,", we have a problem.")
