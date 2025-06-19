# Basicloops.py - the very basics of while loops
#Matthew Raines, COP 2500

'''A WHILE loop has the form:

while <condition>:
    actions
    more actions
    even more actions'''

#Start at 10 and print the integer sequence until 30, by threes.

i=10

while (i<30):
    print(i)
    i=i+3

'''The effect of a while loop is to repeatedly:
* Test whether the control expression is true
* Executes the control block if true
* If it's not true, the loop ends

This means you want the condition to START true (or the code block won't
execute at all), and remains true for some period of time (otherwise use if),
but eventually becomes Not true, or false.'''

'''This means Three things:

* YOu almost always need an initialization statement to set things up. Ex:(i=10)
The condition should be true after the initialization statement, except rare
occasions.

* Your condition must become false eventually, or the loop will be endless.

* Something about what happens inside the loop must change the condition so that
it will eventually FALSE. If you never change the control variable, the loop
will be endless.'''


# EXERCISE ---

j=23

while (j<=100):
    j=j+5
    if (j%2==0):
        print("The number is",j)

'''We can end WHILE loops with an else statementm wbich will run after the loop
completes - when the condition becomes false'''

i=0

while i<10:
    print("Our number is", i)
    i=i+2
else:
    print("We reached ten")

'''We can stop while loops with the break statement, which immediately exits the
loop.

Break statements should not be the normal, you should expect a while loop to
finish. They represent the first of EXCEPTION HANDLING: How to deal with the
unexpected when it happens.'''

i=0

while (i<100):
    print("Our number is", i)
    i=i+3
    if (i==27):
        print("I HATE THE NUMBER 27. STOP HERE.")
        break
else:
    print("We finished without 27")

#The ELSE block of a while loop doesn't run if the loop is broken, only if
#ended properly. That's the difference between having an else block and putting
#code after the WHILE loop's blocks.

# EXERCISE ---

name=input("What is your name? ")

while (name != "Bob"):
    
    # Check for Joe in the begining to guard from an initial Joe input.

    if name=="Joe":
        print("Goodbye Joe")
        break

    #Neither Bob nor Joe
    
    name= input("Say your name again? ")
else:
    print("Finally, it's Bob!")

#While loops can get messy!
