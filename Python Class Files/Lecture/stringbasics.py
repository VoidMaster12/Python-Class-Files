#stringbasics.py - Basics of strings
#Matthew Raines, COP 2500

#Strings are like ranges - list like objects. Instead of a list of numbers,
#they are a list of characters.

t="01234567890123456789012"
s="the quick brown fox jumps over the lazy dog"

print(s[0])
print(s[1])

#Let's look at all 32 characters

print(t)
print(s)

#Spaces do count as characters

print(s[3]) #That is a space

#In Python, an individual character is treated as a string with length one.
#They don't have their own type.

l=len(s)
print(f"Our string is {l} characters long.")

#We can iterate over a string:
'''for char in s:
    print(char)'''

# ACTIVITY---

def string_counter(string):
    length = 0
    for char in string:
        if char !=" ":
            length = length + 1
    return length

ns = string_counter(s)
print(f"We have {ns} non-spaces in our string.")

#We have CAPITALIZATION FUNCTIONS for strings.

print("Uppercase:", s.upper())
print("Lowercase:", s.lower())
print("Capitalized:", s.capitalize())
print("Title case:", s.title())

#You can CONCATINATE strings just like lists:

s = "The quick brown fox"
s = s + "jumps over the lazy dog"

#We can SPLIT strings into lists:

l = s.split()
print(l)

#Split() creates a list of words, takes each work of its string and makes
#it an element of that list, then returns that list to you. By default, it
#splits on spaces, but it can split on anything.

t="the,quick,brown,fox,jumps,over,the,lazy,dog"

l = t.split(",")
print(l)

#Between splitting, concatinating, reading from the user and reading from
#files, it's easy to end up with strings that have spaces on the left or
#right, called LEADING or TRAILING spaces:

t="    this string has leading and trailing spaces   "

print(t)

#Python has a built-in command to STRIP these spaces:

t=t.strip()
print(t)

#Lastly, we can search and replace strings with the replace() function:

s=s.replace("dog", "cat")
print(s)
