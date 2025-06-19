# dictionary-basics.py - Basics of dictionaries
# Matthew Raines, COP2500

# ACTIVITY---

def monstery_man(mon1,mon2):
    monstery1 = mon1["monsteriness"]
    monstery2 = mon2["monsteriness"]
    if monstery1 > monstery2:
        name = mon1["name"]
        print(f"{name} is more monstery!")
    elif monstery2>monstery1:
        name = mon2["name"]
        print(f"{name} is more monstery!")
    elif monstery1 == monstery2:
        print("Both monsters are the same level of monstery.")

#print_dictionary: print the contents of a dictionary. d must be a dictionary.

def print_dictionary(d):
    for key in d:
        item=d[key]
        print(key,"::",item)

# A Dictionary is like a list, except instead of indexes, items have NAMES.
# Use curly brackets to create a dictionary.

things={}

things["test"]="test item"
things["test2"]="a different test item"
things["quantity"]=3.5

print(things["test2"])
print(things["test"])
print(things["quantity"])

#We can print whole dictionaries, but they're ugly.

print(things)

#We call the name of each item the KEY, and the item the VALUE.
#Structures like dictionaries are often called KEY-VALUE stores.

# If you iterate over a dictionary, you get the keys.

for key in things:
    item = things[key]
    print(key, "::", item)

#But - just like with lists - we can get the item easily enough

print("")

print_dictionary(things)

#Keys are UNIQUE. Give a key a new value, and the old one is replaced.

things["test2"] = "still ANOTHER test item"

print("")

print_dictionary(things)

#To delete a key - and its value - use pop.

things.pop("quantity")

print("")

print_dictionary(things)

#By the way, what we've shown you how to do with dicitonaries and lists before
#applies to literally any mechanism for storing data inside a computer.

#Any DATA STORE must allow you to:

#Create information - Name and set element of the dictionary..

#Update information - Replace an element by name.

#Retrieve information - Get an element by name.

#Delete information - Pop an element by name.

#It's possible to initialize multiple items in a dictionary at once:

monster1 = {
    "name": "spaceduckmon",
    "type": "rubberduck",
    "weight": 0.007,
    "monsteriness": 2.0
    }

monster2 = {
    "name": "spinmon",
    "type": "electricscooter",
    "weight": 14.0,
    "monsteriness": 10.0
    }

#Notive that we've given two small monsters all the same keys! We do this with
#dictionaries often because it lets us pass large amounts of data between
#functions without a lot of parameters.

print("")
print_dictionary(monster1)
print("")
print_dictionary(monster2)

monstery_man(monster1,monster2)
