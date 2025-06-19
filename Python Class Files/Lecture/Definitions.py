#Definitions.py - Basic python language definitions
#COP2500, Matthew Raines

''' In this file we'll covre the definitions of:
Directives
Variables
Statements
Expressions
Blocks

We need to make sure your understanding of them is more concrete.'''

# --- Directives:

import math
'''import is a directive. Directive don't do anything immediately, they're meta
commands. They tell the python interpreter something you want it to do, not the
program directly. This directive says "get the math library."'''

# --- Variables:

'''There are 4 main kinds of variables. So far we used integers, floats, and
strings.

Integers are whole numbers.'''

i=3

'''The = is the assignment operator. Operator refers to +,-,=,/, or %
something that taks operands. Assignment refers to what it does - it assigns the
value 3 into the Variable i.

An operator operates on operands.
Operands are what operators operates on.

3=i doesn't work, assignment is directional. The left side receives the right
side, not vice-versa. "Let i=3"

We refer to the left hand and right hand operands of Binary operators like the
assignment operator, in the obvious way.

i is a variable. 3 is a literal integer, an actual, typed integer, an
unchangeable whole quantity with the number sitting in the code.

It's an error for a literal value to be the left-hand operand of an assignment.

We use i, j and k as simple, obvious variable names for integers. If you've got
more than threem give them real names (rectangle_width). If you lose track of
which variable was which, give one a real name.'''

rectangle_width=5

'''Python programmers use SNAKE CASE for variable names

name_long_variables_like_this   (Snake case; Python, C)
dontnamelongvariableslikethis   (Nobody does this)
DontNameLongVariablesLikeThis   (Capitalized CamelCase; Pascal)
dontNameLongVariablesLikeThis   (CamelCase; Java)

When we assigned 5 into rectangle_width, we implicitly defined rectangle_width.
Before giving a variable a value or defining it, it has no value. If we use a
variable before defining it, an error occurs.

We call setting the initial value of a variable as INITIALIZATION. Some
languages separates definition and initialization; Python doesn't.'''

x=3.0

'''FLOATing point numbers, or decimal numbers, live on the continuous real
number line. There are theoretically infinite real number between 2 points.
In computers this is not the case, all real numbers are stored approximately,
so tnere aren't really initite numbers. This is why rounding errrors occur.'''

# We use x, y, and z for simple float names. If you have more than 3, name them.

S="Hello"

'''Strings are sequences of text that aren't futher interpreted. YOu can ask for
a string to become a number and vice versa, but they aren't naturally quantities
as they're stored. Strings are for humans, not computers

Don't compare a string to a number. It will cause an error or randomly be true
or false.

We use s, t, u for simple string variable names.'''

# --- Statements and Expressions

x=3.0 * 9.0 + 5.0

'''A statement is an actual command to the computer that actually does something
with an actual effect: print, output, etc.

In this statement, the value to the variable x is reset to the value of the
right side of the statement.

The right side is the EXPRESSION 3.0*9.0+5.0. Expressions are code, but they
don't do anything. They are something.

The most obvious is the arithmetic expression. It works mostly the same. The
computer solves 3*9+5=27+5=32.

The computer then stores the value of 32.0 into the variable x. Only the right
can be an expression, the left must be a variable.


<variable> = <expression>

The effect is to take the value into the expression and copy it into the
variable.

Expressions can be found by adding/multipying/dividing/subtracting other
expressions.

Variables can go on the right side:'''

y=x*2.0

'''x serves as a simple expression that returns its current value (32.0) into
the expression on the right side. The value of x is substituted in.

Statements can act as expressions. This causes trouble! Avoid using statements
as expressions.'''

# --- Logical Expressions

if (y>50):
    print("y is greater than 50.")
else:
    print("Nope.")

'''The first thing we're interested in is the y>50
This is a logical expression. This returns our fourth kind of value: a logical,
binary, or BOOLEAN value. It is always true or false.

Whenever you hear about binary logic this is what it means. true/false, yes/no,
one/zero, high/low. Logical expressions only have 2 options

You can set variables equal to boolean result.'''

b=(y>50)
print(b)  #Prints true

if (b):
    print("y is greater than 50.")
else:
    print("Nope.")

#Here's a common mistake:

y==32.0
print(y)

'''This is legal code that doesn't do what we want. The equality operator asks
a question. y does not equal 32, so that expression just says false. The
computer moves on and prints y (64.0). The code does nothing.'''

if y==64.0:
    print ("y is equal to 64!")
    print ("y is totally equal to 64!")

print ("I don't care whether y is equal to 64 anymore.")

''' The indented code is guarded by the if statement's condition. It only runs
if the condition is true.

Blocks can be NESTED within each other. The second if is only checked if the
first is true.'''

if y==64:
    print ("Still 64")
    if y==64:
        print("p5 is easy")
    if y==32:
        print("If this ever runs, something is very, very wrong.")

