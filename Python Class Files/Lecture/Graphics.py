#Graphics.py - Using the turtle
#Matthew Raines

#Importing a library makes the capabilities in that library available to you in
#the program you;re writing.

import turtle

#The first thing we need to do with that library is create a drawing canvas for
#the turtle to draw on. 

my_screen=turtle.getscreen()
my_turtle=turtle.Turtle()

#These commands are case sensitive, don't capitalize the getscreen or the left
#turtle. The my_screen and my_turtle are variable names and can be anything.

#This is a square

'''my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)'''
#The turtle goes forward 50 steps, then turns right 90 degrees. The turtle
#accepts turn radii in DEGREES not radians.

my_turtle.pensize(4)
my_screen.bgcolor("cyan")
my_turtle.pencolor("red")
#This makes the line size to 4, instead of the default 1, makes the background
#cyan, and makes the line color red.

#This is a staircase

'''my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)
my_turtle.left(90)
my_turtle.forward(50)
my_turtle.right(90)
my_turtle.forward(50)'''

#Draw a circle

my_turtle.circle(30,180) #Draws a circle with RADIUS 30, and to draw 180 degrees
#of it (semicircle)

#We can use the goto() command to tell the turtle to go anywhere

my_turtle.penup() #This makes the turtle stop drawing the line.
my_turtle.goto(150,100) #This teleports the turtle to these coordinates
my_turtle.pendown()

my_turtle.setheading(0) #This sets the turtle's heading. 0 is east.

'''goto coordinates look like this:
-x,+y                         +x,+y
                0,0
-x,-y                         +x,-y'''

#We can Fill objects:

my_turtle.fillcolor("red")
my_turtle.pencolor("white")

my_turtle.begin_fill()

my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)
my_turtle.forward(50)
my_turtle.right(45)

my_turtle.end_fill()
