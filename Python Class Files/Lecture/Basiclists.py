#Basiclists.py - Basic list operations
#Matthew Raines, COP2500

#Creating a list

#The list is the first type of COLLECTION - a box which can store multiple
#values.

#We use square brackets and commas separating the items.

our_list=["item1","item2","item3"]
print(our_list)

#In python it's legal to have multiple different kinds of items in one list

#Do NOT do this. You almost always want a list of only one kind of thing.

strange_list=["item1",2,3.01,True]
print(strange_list)

longer_list=["item1","item2","item3","item4","item5","item6"]

#ACCESSING ITEMS----

#This is how we access a single item in a list. The 1 is called the list index,
#or the list subscript.

#Lists start at 0, NOT 1. They are zero-indexed, or zero-counted.

print(our_list[0])
print(our_list[1])
print(our_list[2])

print("Negative indexing", longer_list[-2])

#You can use negative indices to walk backward from the right of the lest
#instead of forward from the left.

shorter_list=longer_list[1:4]

print("Short",shorter_list)

#Ranges are inclusive on the left, exclusive on the right. The 4 in 1:4 is
#excluded, so it only prints items 2-4, not 2-5.

#We don't have to access the list in order, we can use whatever order we want.

#ADDING ITEMS----

#There are two good ways to add lists.

#First is to append them to the END of the list. This just adds it on to the end
#of the list. This is the fastest way to add items to the list; whenever order
#doesn't matter you should append.

print("Appending item 4:")
print (our_list)
our_list.append("item4")
print(our_list)

#INSERTING ITEMS----

our_list.insert(2,"item2.5")
print("Insertion:", our_list)

#The insertion goes before the item in the indicated place and is added to the
#list.

#DELETING ITEMS----

#We can REMOVE by value

our_list.remove("item2.5")
print("Deletion:", our_list)

#Or POP items by subscript

our_list.pop(2)

print("Deletion by subscript:", our_list)

#CREATING AN EMPTY LIST----

#If we create a new empty list, we just use empty brackets.

print("Empty list:")
new_list=[]
print(new_list)

#We do this for patterns where we have to initialize a list before starting to 
#add to it. This is often used in loops. Empty lists are analogous.

#FIND ITEMS----

print("---")

index_of_4=longer_list.index("item4")
print(index_of_4)

#The index function searches the list for the parameter, and returns the index
#that the parameter lies.

#index_of_maybe=longer_list.index("maybethere")
#print(index_of_maybe)

#CAUSES AN ERROR

#Using the IN operator safeguards the code from having an error.

if "maybethere" in longer_list:
    index_of_maybe=longer_list.index("maybethere")
    print(index_of_maybe)
else:
    print("Nope")

#Checking where an item is where it's expected is a common pattern to avoid
#bad inputs

#ACTIVITY----

#list_modifier: Given a list and 2 values, deletes the first value and appends
#the second. Returns the new list. Causes an error if the first value to be
#deleted isn't on the list, or if it's not given a list.

def list_modifier(the_list,delete_value,add_value):
    the_list.remove(delete_value)
    the_list.append(add_value)
    return the_list

#list_modifier(our_list,"item1","item4")

#WEEKEND ACTIVITY----

def list_check(l,value):
    if value in l:
        index_l=l.index(value)
        print("Index:",index_l,"\nValue:",value)
    else:
        print("Sorry, that value is not in the given list.")

list_check(our_list,"item2")

print("our_list:",our_list)
print("shorter_list:",shorter_list)
print("longer_list:",longer_list)

#CONCATINATING LISTS

#To concatinate is to write one thing after the other. Bob and cat give bobcat.

#Using the + operator, we can concatinate lists.

reallylonglist=our_list+shorter_list+longer_list
print("reallylonglist:",reallylonglist)

#Sorting a list works almost exactly the way you expect. At base, call the list
#sort() function and Python will do its best to order the lists.

reallylonglist.sort()

print("Sorted reallylonglist:",reallylonglist)
