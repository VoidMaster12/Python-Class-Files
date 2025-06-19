#basicinput.py - Basic Python input
#Matthew Raines, COP2500, Spring 2022

#We will do INPUT - to ask the user for values to work with
myname= input("What is your name?")
print("Hello,", myname)

'''The input command uses whatever string you give it as a prompt, and returnes,
or makes available, whatever the user enters.
We refer to this as terminal input - in a broadest sense, this means input
taken at the terminal point of all the computers and networks between the
program and the user. It refers to text-only programs. Command prompt works
like traditional physical terminals like how we interacted with computers.'''

'''We can also input numeric values to use in math - but for that, we need to do
extra work.'''
#x=input("What should I add to 3?")
#print("3+x=", 3+x)
'''This doesn't work because the type of value input() returns is always a
STRING - is always text. We can enter a number, but Python doesn't know it's a
number.
We have to tell Python that we want an integer, or a whole number'''

x=int(input("What should I add to 3?"))
print("3+x=", 3+x)

#This forces the user's input to become an integer. If we don't enter a number,
#it breaks.

i=int(input("What should I add to 3?"))
print("3+i=",3+i)

#We can do this with a decimal, or floating point:

x=float(input("What should I add to 3.1416?"))
print("3.1416+x=", 3.1416+x)
