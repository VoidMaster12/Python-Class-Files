#vehicle.py - Turtle drawing a vehicle
#Matthew Raines

#This was created to draw a vehicle using turtle graphics. Hopefully it doesn't
#look horrible, art is not my strong suit.

import turtle
screen=turtle.getscreen()
tur=turtle.Turtle()

tur.pensize(2)
screen.bgcolor("cyan")

tur.penup()
tur.goto(50,-50)
tur.pendown()

tur.setheading(90)

tur.fillcolor("silver")
tur.begin_fill()

tur.forward(50)
tur.right(90)
tur.fd(80)
tur.left(70)
tur.fd(100)
tur.rt(70)
tur.fd(200)
tur.rt(90)
tur.fd(165)
tur.rt(90)
tur.fd(315)
tur.rt(90)

tur.pencolor("yellow")
tur.fd(40)

tur.end_fill()

#These are the headlights, they are yellow. It doesn't look as good as I hoped.

tur.fillcolor("yellow")
tur.begin_fill()

tur.lt(80)
tur.fd(200)
tur.setheading(270)
tur.fd(80)
tur.lt(90)
tur.fd(200)

tur.end_fill()

#These are the wheels.

tur.pencolor("black")
tur.fillcolor("black")
tur.penup()

tur.fd(100)
tur.rt(90)
tur.fd(20)

tur.pendown()

tur.begin_fill()
tur.circle(30)
tur.end_fill()

tur.penup()
tur.setheading(0)
tur.fd(130)
tur.setheading(270)

tur.pendown()

tur.begin_fill()
tur.circle(30)
tur.end_fill()

#This is the best art I've ever made in my life.
