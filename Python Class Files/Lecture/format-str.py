#format-str.py - Formatting strings
#Matthew Raines, COP2500

import math

#Formatting strings are the simplist way to generate better numeric output.
#They're ugly.

print(math.pi)

our_pstr=f"pi= {math.pi:.4f}"
print(our_pstr)

#Formatting strings have a lowercase f which stands for formatting. They can
#contain format specifiers in curly braces. Everything outside the braces is
#interpreted and printed normally.

#A FORMAT SPECIFIER takes the form:

'''{<value>:<instructions>]'''

#The value part is easy, it's almost always a variable. (Do not call functions
#inline in a format specifier.

#{math.pi:.4f}

#The value is math.pi. Most versions of python show pi as 3.141592653589793,
#which is the best approximation of pi in a double-precision floating point
#number.

#The ".4" part of the instructions tells the formater we want 4 DIGITS to the
#RIGHT of the decimal point. PYTHON WILL ROUND CORRECTLY! Python also pads it
#with zeroes on the right:

print(f"{3.4:.8f}")

#This is how you mask rounding errors.


#The f part tells Python to format this as a floating point number. Leaving out
#the f after the .4 isn't an error but it makes the result less predicable.

y=1048576.1048576

print(f"pi = {math.pi:.4f}")
print(f"y = {y:.4f}")

#We can get proper allignment - decimal points in the same place - by giving a
#FIELD WIDTH along with the number of significant digits. The field width goes
#to the left of the decimal point.

print("")
print("       12345678901234567890")
print(f"pi = {math.pi:15.4f}")
print(f"y =  {y:15.4f}")

#The 15 is the total space for the entire number, NOT just the number of digits
#to the left of the decimal. Of our fifteen:

#4 are used for the fractional part
#1 is used by the decimal point
#The other 10 are available for the whole number part.

#The numbers get alligned on the decimal point.

#with this kind of formatting, negative numbers pretty much take care of
#themselves.

z=-y
print(f"z =  {z:15.4f}")

#To force the positive sign to appear, put a plus before the f

print(f"y =  {y:+15.4f}")

#Replace the f with an e for scientific notation. The precision is the number
#of digits after the decimal point.

print(f"y =  {y:15.4e}")

#Lastly, Python has a nice option for large numbers: it can insert commas for
#you. It goes after the field width, before the decimal point.

print(f"y =  {y:15,.4f}")
