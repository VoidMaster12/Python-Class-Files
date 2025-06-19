# Forloops.py - basic FOR loops
# COP2500

# A FOR loop, instead of being based on a condition, is based on a list of
# things.  The idea is "for each of these things, do this".  The form is:

# for <variable> in <list>:
#   do stuff
#   do more stuff
#   and so on

# We will teach you *much* more about how to make various kinds of lists in
# Python later.  Right now, we're going to work with the simplest kind of
# list: the integer numeric RANGE.

print ("")

for i in range(1, 10, 1):
    print (i)

# The LOOP VARIABLE i is set to each value in the integer RANGE from 1 to 10 -
# but there's an important point you need to know about Python ranges:

# Ranges are INCLUSIVE on the LEFT.   The left uses >=.
# Ranges are EXCLUSIVE on the RIGHT.  The right uses <.

# So this is the integer range [1, 10) instead of [1, 10]: in other words,
# 1 through 9.  If we want 1 through 10:

print ("")

for i in range(1, 11, 1):
    print (i)

# The third parameter is the STEP parameter.  We don't actually have to visit
# every number in the range.  This is best shown by example:

print ("")

for i in range(1, 100, 7):
    print (i)

# So the range has the form:

# range(low, high, step)

# where:
# low is the left of the range, inclusive (low IS in the range)
# high is the right of the range, exclusive (high is NOT in the range)
# step is the number by which we increment each, well, step

# EXERCISE: Write TWO for loops, using two DIFFERENT techniques, to print all
# of the numbers from 1 up to and including 99 that are divisible by three.

for i in range(1, 100, 1):
    if i % 3 == 0:
        print (i)

for i in range(3, 100, 3):
    print (i)

# In this case, the second method is actually, and actively, better than the
# first one.  In the first method, the computer has to examine every number
# between 1 and 99 and reject the ones we didn't want it to print - and those
# tests and rejections take time.

# In the second method, the computer is only given the correct numbers to begin
# with, so it can get straight to the business of printing them.

# When code does the same job while requiring the computer to take fewer steps,
# we say that code PERFORMS better, or is better-PERFORMING code.  There are
# whole branches of computer science that study how well code performs.

# DON'T WORRY MUCH ABOUT THE PERFORMANCE OF YOUR CODE YET.  As long as it runs
# in a reasonable amount of time, for this class, it's fine.  Correctness is
# always more important than performance, and in this class you will mostly be
# concerned with correctness.






