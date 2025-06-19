import time

# lineplotter.py - Plotting a linear function
# Matthew Raines COP2500

# This program was written to plot a linear function.

# This takes the input for the slope and intercept

m=float(input("Enter the slope of the line: "))
b=float(input("Enter the y-intercept: "))

start_time = time.time()

#This prints the formula for the line

print("Linear Function: y =",m,"x + ",b)

#This calculates and prints the x and y values from 0-9
for x in range(0,10,1):
    y=m*x+b
    print("At x=",x,", y=",y)

#This starts at x=10 and prints the x and y values for powers of 10 up to 100000

x=10

while x>=10 and x<=100000:
    y=m*x+b
    print("At x=",x,", y=",y)
    x=x*10

print(f"Run time: {time.time() - start_time} seconds.")
