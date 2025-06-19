#conditionals.py - Basic conditional statements
#Matthew Raines

#A conditional statement is something you tell python to do if something is true
#If, then, else. If this, then that, else that.

x=300
y=500

print(x)
print(y)
if x>y:
    print("x is greater than y")
else:
    print("x is not greater than y")

#The else runs ONLY if the condition is false

if y>x:
    print("y is greater than x")
else:
    print("Nuh uh")

#You MUST indent the code that you want to be conditional

'''if statements let us control the flow of control. When the condition fails,
we skip it. The block of code guarded by if statements run only if the
condition is true'''

#The form of an if statement is:

'''If(condition):
    do that action
    and that action
else:
    do something else'''

'''The basic conditions are:
== equality - 2 equal signs, check if something is equal. = sets it equal
    to that value (causes an error)
!= inequality - "not equal to"
< Less than
> Greater than
<= Less than or equal to
>=greater than or equal to'''

#Equality/Inequality also work on strings (text, not numbers)

bob="Bob"
if(bob=="Bob"):
    print("Yep, that's Bob.")
else:
    print("Evidently, that's not Bob.")

if(bob=="bob"):
    print("That's Bob.")
else:
    print("Not Bob, (It's bob)")

#Comparisons are case-sensitive with strings

entered_name=input("What is your name? ")

if(entered_name=="Bob"):
    print("Greetings, you are Bob!")
else:
    print("You are not Bob; hello.")

#IF statements can use compound conditionals as what they test, not just simple
#inequalities

if (entered_name=="Alice") or (entered_name=="alice"):
    print("Oh, wait, it's Alice! Hi, Alice!")

#To use OR or AND properly, you must modify the entire comparison.
#if (entered_name=="Alice" or "alice"): DOES NOT work

'''The three basic compound conditions are:
and - true if and only if both halves are true
or - true if either or both halves are true
not - true if and only if its parameter is false'''

#These are called the basic logical operations, or BOOLEAN operations

entered_name=input("Tell me your name again? ")
print("You said:",entered_name)

if not (entered_name=="Bob"):
    print("I have decided you are NOT Bob.")

entered_name=input("Tell me your name ONE more time? ")
print("You said:",entered_name)

if (entered_name=="Bob"):
    print("You're Bob. I thought we established this already.")
elif (entered_name=="bob"):
    print("Hey, Bob. You're quiet today.")

#elif means else-if. If the IF were to fail, it tests if ELIF is true. If ELIF
#is true then it runs. If it's not true then neither will run. At most ONE of
#of the blocks will run.

#EXERCISE

num=int(input("Give me a whole number!\n"))

if (num>=0) and (num<10):
    print("Your number is a unit digit, how disappointing.")
elif (num<100):
    print("Your number is a tens digit...")
elif (num<1000):
    print("Your number is a hundreds digit.")
elif (num<10000):
    print("Your number is a thousands digit!")
elif (num<100000):
    print("Your number is a tens-thousands digit!!")
elif (num<1000000):
    print("Your number is a hundred-thousands digit!! :)")
elif (num<0):
    print("That number is negative!")
else:
    print("That is a very large number!")
