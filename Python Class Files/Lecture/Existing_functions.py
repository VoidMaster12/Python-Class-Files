#Existing_functions.py - Documentation for existing functions
#Matthew Raines, COP2500

'''The print function accepts one or more strings as parameters and prints them
to the terminal. It will try to convert things that aren't strings to string.
If it can't, it causes an error.'''

print("Three:",3)

'''The input function accepts a prompt string and asks the user for input at the
terminal ending with the ENTER or RETURN key. It returns the input provided,
always as a string.'''

s=input("Enter something: ")
print("You entered,",s)

'''The int function tries to convert its parameter to an INTEGER, or whole
number. If it can, it returns that integer; if it can't, it causes an error.'''

three=int(3)
#error=int("three")     This does not work

'''The float function tries to convert its parameter to a FLOATing point number,
or a decimal. If it can, it returns that float; if it can', it causes an
error.'''

three_point_zero=float("3")
also_three_point_zero=float(3)
