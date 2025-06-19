#quadplotter.py - Quadradic graphing
#Matthew Raines, COP2500

#This was written to print the coordinates of a quadratic function to practice
#with quadratics.

#calc_coords: Calculates the y value for a certain x value given the coefficients
#for a quadratic function. Returns the y value. Causes an error if the user
#doesn't enter a number for the coefficients, or if x isn't a number.

def calc_coords(x,a,b,c):
    y=a*x**2+b*x+c
    return y

#print_coords: Calls upon calc_coords and prints the x and y coordinates given
#the x coordinate and the coefficients for the quadratic. Returns nothing.
#Causes an error if the user doesn't enter a number for the coefficients, or if
#x isn't a number.

def print_coords(x,a,b,c):
    y=calc_coords(x,a,b,c)
    print("At x=",x,", y=",y)

#Main Program Begins Here-----

#Gets the a, b, c value from the user.

a=float(input("Enter the value for coefficient a: "))
b=float(input("Enter the value for coefficient b: "))
c=float(input("Enter the value for coefficient c: "))

#Prints the function

print("The function is:",a,"x^2 +",b,"x +",c)

#Calls the print_coords function for x values 0 to 9.

x=0
for x in range(0,10):
    print_coords(x,a,b,c)

#Calls the print_coords function for x values 10 to 10 million by powers of ten.

x=10
while x<=10000000:
    print_coords(x,a,b,c)
    x=x*10
