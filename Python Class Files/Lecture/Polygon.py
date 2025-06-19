#Polygon.py
#Matthew Raines, COP2500

#Defines the function for the polygon

def drawPolygon (tur,x,y,sides,perim):
    #Brings the turtle to the coordinates
    tur.penup()
    tur.goto(x,y)
    tur.pendown()
    #Calculates the side length and angle
    side_length=perim/sides
    angle=360/sides
    #Moves the turtle
    for i in range (1,sides+1,1):
        tur.fd(side_length)
        tur.rt(angle)

#Initializes the turtle

import turtle
screen=turtle.getscreen()
tur=turtle.Turtle()
screen.bgcolor("cyan")

#Asks for input and calls the funtion. If there's 8 sides, it draws a stop sign

x=float(input("Enter starting x coordinate: "))
y=float(input("Enter starting y coordinate: "))
sides=int(input("Enter the Number of sides: "))
perim=int(input("Enter the perimeter: "))

if (sides==8):
    tur.pencolor("white")
    tur.fillcolor("red")
    tur.begin_fill()
    drawPolygon(tur,x,y,sides,perim)
    tur.end_fill()
else:
    drawPolygon(tur,x,y,sides,perim)
