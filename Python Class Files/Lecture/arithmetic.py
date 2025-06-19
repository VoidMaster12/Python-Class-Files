# arithmetic.py - Basic arithmatic examples
# Matthew Raines, COP2500

# This is a header Comment. Lines starting with the hash are ignored by python.

x = 3.2
y = 5.4

i = 3
j = 5
print("Our value x is equal to:", x)
x = 3.8
print("Our value x is equal to:", x)

# Variables can change value as the program moved down.

print("Our value y is equal to:", y)

# Only the variable outside the quotes is recognized.

print("Our value y is equal to:", x) #WRONG!!

# If you try to print something you haven't defined yet, you get an error
# print(z)

z = 1.1 # It has to be in chronological order, so z has no value until after the

# previous line tries to print z

print(x + y, "is the sum of x and y.")

# We often want to compute results then output them

z = x + y
print(z, "is the sum of x and y.")

# We don't need to mention z, it's up to us to match the result and description

k = j - i
print("j-i=",k)

#Negative numbers work as well

k = i - j
print("i-j=",k)

z = y - x
print("y-x=",z)

k = i * j
z = x * y

print("i*j=", k)
print("x*y=", z)

k = i / j
z = x / y

print("i/j=", k)
print("x/y=", z)

#Floor division is what you normally get from other languages when dividing
#whole numbers. It's familiar to you as division-with-remainders

k = j//i  #quotient
m = j%i   #remainder

print("j/i  quotient=", k)
print("     remainder=", m)

#PEMDAS is normal, parenthesis work normally.

z = x + y * y
a = (x + y) * y

print("x+y*y=", z)
print("(x+y)*y=" , a)

#Using ** is like the ^, it exponentiates (raises the number to that power)

k = 2**8
print("2^8=",k)

#2^10 is the base-2 version of "kilo" - the number of bytes in a kilobyte. We
#use it because at 1,024, it's very close to 1,000 -  the metric k.
#The discrepancy between base-2 and base-10 versions of K is the root of the
#discrepancy between advertised and reported disk drive capacity.

k = 2**10
print("2^10=", k)

#2^20 is base-2 version of "mega"

k=2**20
print("2^20=", k)

#2^30 is base-2 version of "giga"

k=2**30
print("2^30=",k)

#2^40 is base-2 version of "tera"

k=2**40
print("2^40=",k)

#8, 16, 32, and 64-bit computers and consoles refers to how large an integer
#number the CPU can add without performing a carry operations.

#When these bit widths are used for memory addressing, they can also limit how
#much memory the computer can access. True 16-but computers were limited to 64k
#of primary memory; most 32-bit were limited to 4gb. Limits of 64-bit won't be
#relevant anytime soon.

k=2**8
print("2^8=",k)

k=2**16
print("2^16=",k)

k=2**32
print("2^32=",k)

k=2**64
print("2^64=",k)
