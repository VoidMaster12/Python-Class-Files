#oddeven.py - Playing the odd even game
#Matthew Raines

#This was created to play the odd even game by generating a random number and
#asking the user to guess whether it's odd or even

import random

x=random.randint(1,256)

z=x%2

guess=input("I have a number, guess if it's even or odd!\n")

if (z==0) and (guess=="even"):
    print("Good job, it was even! The number was",x,".")
elif (z==0) and (guess=="odd"):
    print("Oh no! It was even :(. The number was",x,".")
elif (z==1) and (guess=="even"):
    print("Foiled again! It was odd :(. The number was",x,".")
elif (z==1) and (guess=="odd"):
    print("Nice, it was odd! The number was",x,".")
else:
    print("You didn't say odd or even. Oh well...",x,"was my number.")
