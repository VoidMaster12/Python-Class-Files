# tupleset.py - Tuples and sets in Python

# --- TUPLES ---

# A TUPLE is like a list except it can't be changed once it's created.  Think
# of things like ordered pairs or ordered triples, coordinate groups that are
# treated like single objects.

# Create a tuple like a list, but use parentheses instead of square or curly
# brackets.

my_tuple = (3.0, 5.0, 7.0)

print (my_tuple)
print (my_tuple[1])

# my_tuple[1] = 4.0 - error!
# print (my_tuple)

# Tuples can't be changed once they're created.  If you want to change an
# element of a tuple, you have to make a new tuple.

# Tuples are the only kind of IMMUTABLE COLLECTION - they are passed by VALUE
# to a function and COPIED on assignment, instead of being passed or assigned
# by reference.

# You can iterate normally over a tuple, or its indices.

for x in my_tuple:
    print (x)

# A tuple is a good way to "pack" values - there's even a shorthand syntax
# for pulling all the values out of one.

(x, y, z) = my_tuple
print (x)
print (y)
print (z)

print ("---")

# --- SETS ---

# A SET is like a list, but it's not ordered and it can't have duplicates.  To
# create a set, use curly braces, but give a flat set of items instead of using
# dictionary syntax.

# my_dictionary = {"name": "Bob"}

my_set = {"thing1", "thing2", "thing3"}
print (my_set)

# You can't create an empty set with curly braces; if you do that you just get
# an empty dictionary.  To create an empty set, use set().

my_empty_set = set()

# Since they aren't ordered, sets DO NOT have indexes.

# print (my_set[1]) - error!

# We can add and remove from sets...

my_set.add("thing4")
my_set.remove("thing2")
print (my_set)

# ...and they can't hold duplicates.  Adding a duplicate does nothing.

my_set.add("thing4")
print (my_set)

# If you want a remove()-alike that doesn't cause an error when removing
# something that isn't there, you can use discard().  discard() TRIES to remove
# the object from the set, and just ignores it if it isn't there.

# my_set.remove("not in the set") - error
my_set.discard("not in the set") # silently fails
print (my_set)

# Sets don't have indexes, but we CAN iterate over them.  The order, like
# everything else with sets, is random!

for x in my_set:
    print (x)

print ("---")

other_set = {"thing2", "thing3", "thing5"}
print ("Set A:", my_set)
print ("Set B:", other_set)

# The UNION of two sets contains all the objects in either set.

print("A union B:", my_set.union(other_set))

# The INTERSECTION of two sets contains the objects common to both.

print("A intersect B:", my_set.intersection(other_set))

