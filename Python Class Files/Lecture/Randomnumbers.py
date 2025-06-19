#Randomnumbers.py - Basics of random numbers
#Matthew Raines COP2500

'''A random number is a number you don't know the value of before you ask for
it. It's like rolling a die.'''

import random

#Use the random.randint function. It returns a random integer between and
#including it's parameters.

x = random.randint(1,256)

print("We got",x)

#The random numbers are NOT weighted in any way by default.
