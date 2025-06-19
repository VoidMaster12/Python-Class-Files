#Functions.py - function definitions
#Matthew Raines- COP2500

# Functions are subcode, they are their own universe of code.

''' The functions here don't do much. However, they show a general pattern of
functions, which has two advantages:

*They avoid repeating code. You don't need to rewrite the equation for a line

*It makes finding BUGS easier. Here we only compute the equation of a line in
one spot. If the results are wrong, there's only one possible place where it
went wrong.'''

'''The form of a function definition is:

def funtion_name(parameter_1,parameter_2,...):
    code block

Defining the function does NOT execute its code. The code block is only executed
when the function is CALLED.

The code block is executed when the function is called. The code block can
include return statements - these only make sense in fucntions.'''

'''when you send a function its parameters, they're positionally substituted in
the ORDER THEY APPEAR in the function header. The name doesn't matter, ONLY the
order. Our first call of 1,3,5 sends:

slope= 1 (first parameter)
intercept= 3 (second parameter)
x=5 (third parameter)'''

'''A funtion ONLY knows its parameters. It can't see the variables that make up
the main code. The main program has to send the variables as parameters for the
function to use them. The variables are OUT OF SCOPE.

The RETURN statement tells the function the value it should TAKE ON. When a
return statement is executed, the function stops, and the return value is
substituted in for the funtion itself at the point the function was called.'''

def linepoint(slope, intercept, x):
    y= slope * x + intercept
    return y

'''Functions don't actually have to return values, some are designed to more
imperitive commands: they do specific things'''

def print_line_result(x,y):
    print("Our results are:",x,y)

def compute_and_print(slope,intercept,x):
    y=linepoint(slope,intercept,x)
    print_line_result(x,y)

# Main program begins here.

'''The part of the program that is not a function - that gets run immediately.
In python, the main program must follow the function.'''

#Here we CALL the function with parameters 1,3, and 5 to obtain a value.
#We print that value. When linepoint() returns its y value, that value is
#substituted in here for linepoint(), giving our_value the returned value.

m=float(input("Enter the slope: "))
b=float(input("Enter the y-intercept: "))
print("Enter 0 for x to quit")
x=float(input("Enter the x value: "))
#our_value=linepoint(m,b,x)

while x > 0:
    compute_and_print(m, b, x)
    x = float(input("Enter the x value: "))


'''The x in our main program is a different variable than the x in our
functions, which are different from each other!

Now we call our printer function. Our printer function doesn't return a value,
so we don't assign any value to its output, we just call upon it.'''

#print_line_results(x,our_value)
