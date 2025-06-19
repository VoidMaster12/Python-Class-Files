#Quadradiclists.py
#Matthew Raines, COP2500

# quadradic: Given the a,b,c coef. of a quadradic and an x value, calculates and
# returns the y value. Causes an error if any parameter isn't a number.

def quadradic(a,b,c,x):
    y=a*x**2+b*x+c
    return y

#output_quad: Given an x and y coordinate, prints the x and y coordinate.
#Returns nothing. Causes an error if the x or y isn't defined.

def output_quad(x,y):
    print("f(",x,")=",y, sep="")

#quad_list: Given the a,b,c coef. of a quadradic and an x value, creates and
#returns a list of y values. Causes an error if any parameter isn't a number.

def quad_list(a,b,c,xlist):
    ylist=[]
    for x in xlist:
        y=quadradic(a,b,c,x)
        ylist.append(y)
    return ylist

#output_quad_list: Given an x and y coordinate list, prints the x and y
#coordinates. Returns nothing. Causes an error if x or y isn't defined.

def output_quad_list(x,y):
    for i in range(len(x)):     #len is the length of the xlist
        output_quad(x[i],y[i])

#----MAIN PROGRAM----

#Gets the a,b,c coefficients
a=int(input("Enter the value for a: "))
b=int(input("Enter the value for b: "))
c=int(input("Enter the value for c: "))

#Calculates and prints the x and y values
x=list(range(10))       #Sets the list of x values to all values 0 to 9.
i = 10
while i <= 100000000:
    x.append(i)
    i=i*10

y = quad_list(a,b,c,x)
output_quad_list(x,y)
