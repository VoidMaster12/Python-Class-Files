#Function-scope.py - Function parameters and variable scope
#Matthew Raines, COP2500

#Notice that this results in an error. Even though we're defining x in
#some_function. That variable is out of scope for the main program.

#def  some_function():
#    x=3.0

#some_function()
#print(x)

'''Variables have a scope. Variable's don't generally survive the return of the
function the defines them -  when the function is returned, its defined
variables go out of scope and are extinguished.

So in the above example, when some_function() is called, the x that was
defined in it disappears. The main program gets an error when trying to read x,
because it doesn't know one.'''

#def some_function():
#    print(x)

#x=3.0
#some_function()

'''Here, referring to x in some_function works even though it wasn't defined at
the time the function was defined. In python, that's fine as far as the
interpreter is concerned, because it was defined when the function was called.

Since x is defined in the main program, it's still defined when the function is
called.

MOST LANGUAGES DO NOT ALLOW THIS. DO NOT USE THIS, YOU WILL LOSE POINTS!

There are times where you want to use global variables that every function in
your code sees at once, but they're rare. They're often used for parameters set
only once, or a constant (like math.pi)

If you use global variables, they should be defined at the beginnning of the
program after the imports, before the functions. DO NOT USE THEM for most
situations.'''

#Here's the right way:

#def some_function(print_this):
#    print(print_this)

#x=3.0
#some_function(x)

'''Now we've explicitly passed what we want to print to our function, so we can
easily track it. This is easy to read and makes sense.'''

#This is often seen as well:

def some_function(x):
    print(x)

x=3.0
some_function(x)

'''This does what we expect. The x that is printed is not the x from the main
program, it's the x that was passed to the parameter of the funtion. Just
because they're both x doesn't mean they're the same.'''

#def some_function(x):
#    print("Printing in function:",x)
#    x=5.0
#    print("Printing in function again:",x)

#x=3.0
#some_function(x)
#print("Printing in main:",x)

'''The function's copy of x was changed to 5 after it's printed, but only it's
copy of the x, not the main program's copy. When the function stops running,
it's copy is erased and the main program's x takes back over.

The function's copy of x HIDES the main program's copy of x from the function;
it is closer in scope. The main program doesn't know about it because the
function's x disappears when the function returns.

Use real names for function parameters to avoid this.'''

def some_function(x):
    print("Printing in function:",x)
    x=5.0
    print("Printing in function again:",x)
    return x

x=3.0
y=some_function(x)
print("Printing in main:",y)

'''This allows us to send data back from the function. However, x is still 3,
because the new x was captured by y in the main program.'''

print("One last time:",x)
