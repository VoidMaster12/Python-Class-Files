#copyrel.py
#Matthew Raines, COP2500

i=3
j=i

print(i,j)

i=i+1

print(i,j)

print("---")

#Lists don't work like that. When we assign a list to another list, we're not creating a copy, we're assigning a REFERENCE. The second
#variable, mylist2, becomes a second name for the first list, not a copy of the list.

mylist=["bob","carol","dave","alice"]

mylist2=mylist.copy()

print(mylist)
print(mylist2)

mylist.remove("alice")

print(mylist)
print(mylist2)

print("---")

def change_list(thelist):
    thelist.pop(1)
    print("Inside function, the list is: ",thelist)

mylist=mylist=["alice","bob","carol","dave"]
print(mylist)
change_list(mylist)
print(mylist)

#Functions actually change the list without returning them. The function gets a referece of the list, and the function can actually
#change that.

#The rule is that immutable objects are assigned and passed by copy, and MUTABLE objects are assigned and passed by referece.

# *Atomic* variables like ints, floats, strings are immutable.
# Complex containers like lists and dictionaries are mutable, and will change if you change the copy. TUPLES are an excpetion.
#Complex non-containers like turtle are also mutable.

#---------

# You can override this by using the copy() function

