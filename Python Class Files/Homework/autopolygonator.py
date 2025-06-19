# autopolygonator.py - Drawing polygons
# Matthew Raines COP2500

# This was written to generate polygons given total length because polygons are
# cool.

# Imports turtle and asks for number of sides and total length

import turtle
import time

sides = int(input("Enter number of sides: "))
length = int(input("Enter total length: "))

# Calculates the length of each side and degrees to turn given the total length
# and number of sides

side_length = length/sides
angle = 360/sides

# Sets up the turtle

screen = turtle.getscreen()
tur = turtle.Turtle()
screen.bgcolor("cyan")
tur.pensize(2)

# Draws the polygon

for i in range(1, sides + 1, 1):
    tur.fd(side_length)
    tur.rt(angle)
