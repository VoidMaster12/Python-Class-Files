#Lineplotter.py - Plot a line at several coordinates
#Matthew Raines, COP2500

#compute_linear: Given the slope, y-int, and an x coordinate, calculates and
#returns the y value. All parameters must be numbers.

def compute_linear(m,b,x):
    y=m*x+b
    return y

#Compute_linear_list: Given the slope, y-int, and a list l of x coordinates,
#calculates a list of y coordinates and returns them. m and b must be numbers,
#and l must only have numbers.

def compute_linear_list(m,b,l):
    ylist=[]
    for x in l:
        y=compute_linear(m,b,x)
        ylist.append(y)
    return ylist

#Given the input and results lists, prints the lists in parallel. Returns
#nothing. Both lists must be numbers and of equal length.

def print_parallel_lists(xl,yl):
    for i in range(len(xl)):
        x=xl[i]
        y=yl[i]
        print(f" x={x:10,.2f}, y={y:10,.2f}")

#MAIN PROGRAM----

#Gets the slope and intercept.

m=float(input("Enter the slope: "))
b=float(input("Enter the intercept: "))

#Defines the xlist for the x values we cant to calculate.

xlist=list(range(0,10))
elist=[10,100,1000,10000,100000]
xlist=xlist+elist

#Computes and prints the coordinates.

ylist=compute_linear_list(m,b,xlist)

print_parallel_lists(xlist,ylist)
