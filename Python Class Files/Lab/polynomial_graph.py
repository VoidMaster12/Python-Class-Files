# polynomial_graph.py - Graphs a quadratic given the a, b, c coefficients.
# Matthew Raines

import turtle
import time

def draw_axis():
    turtle.goto(-400, 0)
    turtle.goto(400, 0)
    turtle.goto(0, 0)
    turtle.goto(0, 400)
    turtle.goto(0, -400)

# convert_list_to_floats: Given a list, converts all items to floats and
# reverses the order for graphing. All items must be numbers.

def convert_list_to_floats(list):
    for i in range(len(list)):
        list[i] = float(list[i])
    list.reverse()

# goto_start: Given the x and y lists, goes to the first coordinate without
# drawing anything. 

def goto_start(x_list, y_list):
    turtle.penup()
    turtle.goto(x_list[0] * mag, y_list[0] * mag)
    turtle.pendown()

# Given an x and the list of coefficients, calculates and appends the y value
# to the y list.

def calc_and_append(x, coeff_list):
    y = 0
    for i in range(len(coeff_list)):
        y += coeff_list[i] * x**i
    y_list.append(y)

# ---MAIN---

# Sets up x and y lists

x_list = []
y_list = []

# Gets the coefficients and makes the list a list of ints

coef = input("Enter the coefficients for a polynomial function in the format 'a,b,c,...': ")
coeff_list = coef.split(',')

convert_list_to_floats(coeff_list)

# Calculates points and adds them to a list

x = -5

while x <= 5:
    x_list.append(x)
    calc_and_append(x, coeff_list)
    x += 0.1

# Sets up turtle

screen = turtle.getscreen()
screen.bgcolor('cyan')
turtle.pensize('2')
turtle.speed(0)
mag = 20

# Graphs

draw_axis()

goto_start(x_list, y_list)

for i in range(len(x_list)):
    x = x_list[i] * mag
    y = y_list[i] * mag
    turtle.goto(x, y)

print("Done graphing.")
time.sleep(3)
