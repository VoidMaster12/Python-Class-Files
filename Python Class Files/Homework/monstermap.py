#monstermap.py - Drawing maps of distribution
#Matthew Raines, COP2500

#This was created to show the distribution of small monsters to help me catch
#them all!

#Imports the turtle
import turtle

#turtle_mover: Moves the turtle without drawing anything given the horizontal
#and vertical cell and a turtle. Returns nothing. Causes an error if the
#horizontal or vertical cell isn't a number.

def turtle_mover(t,horiz_cell,vert_cell):
    t.penup()
    t.goto(25*horiz_cell,-25*vert_cell)
    t.pendown()

#draw_circle: Given a turtle, horizontal and vertical multiplier and constant,
#and the vertical cell number, moves the turtle across the horizontal row and
#draws a circle with the radius found by the formula below. Causes an error if
#any of the parameters excluding the turtle isn't a number.

def draw_circle(t,horiz_mult,vert_mult,vert_cell,constant):
    horiz_cell=1
    for horiz_cell in range(1,11):
        turtle_mover(t,horiz_cell,vert_cell)
        t.begin_fill()
        t.circle(horiz_mult*horiz_cell+vert_mult*vert_cell+constant)
        t.end_fill()

#----Main Program----

#Sets up turtle
    
tur=turtle.Turtle()
screen=turtle.getscreen()
tur.fillcolor("cyan")
tur.speed(0)

#Gets the horizontal multiplier, vertical multiplier, and the constant.

horiz_mult=float(input("Enter horizontal multiplier: "))
vert_mult=float(input("Enter vertical multiplier: "))
constant=float(input("Enter a constant: "))

#Moves the turtle and draws a circle for each cell location.

horiz_cell=1
vert_cell=1

for vert_cell in range(1,9):
    draw_circle(tur,horiz_mult,vert_mult,vert_cell,constant)
