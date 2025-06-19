#Quadradic Graphing.py
#Matthew Raines COP2500

#Initializing Turtle

import turtle
tur = turtle.Turtle()
screen = turtle.getscreen()
tur.pensize(2)

#Take a, b, and c input

a = float(input("Enter the a value: "))
b = float(input("Enter the b value: "))
c = float(input("Enter the c value: "))

# This moves the turtle to the first coordinate without drawing an extra line.

x = -20
y=a*(x**2)+b*x+c

tur.penup()
tur.goto(x,y)
tur.pendown()

# This calculates the x and y values and graphs the curve.

while x >=- 20 and x <= 20:
    y = a*(x**2)+b*x+c
    tur.goto(x,y)
    x = x + .5
