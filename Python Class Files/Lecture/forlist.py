#forlist.py
#Matthew Raines, COP2500

longer_list=["item1","item2","item3","item4","item5","item6"]
print(longer_list)

#Ranges are almost like lists...

ourrange=range(1,10,1)
print(ourrange)

#...and can be turned into lists.

ourrangelist=list(ourrange)
print(ourrangelist)

#We know we can loop over a set range in a for loop.

'''for i in range(1,10,1):
    print(i)'''

#We can also loop over a previously defined range.

'''for i in ourrange:
    print(i)'''

#We can also loop over the LIST

'''for i in ourrangelist:
    print(i)'''

#We can loop over the list itself. This is the real use of the FOR loop.

for s in longer_list:
    print(s)

#Form of a for loop:

'''for <item> in <list>:
    do something'''

#The for statement defines the item for you repeatedly as it goes through the
#list, executing the code block for each item.

#ACTIVITY:

#summation: Given a list, calculates the sum of the list and returns it. Causes
#an error if the list has strings.

def summation(thelist):
    the_sum=0
    for i in thelist:
        the_sum=the_sum+i
    return the_sum

#If we need the index as well as the value of the item, we can loop on the
#index instead of the value.

for index in range(0,len(longer_list),1):
    item=longer_list[index]
    print("The item as index",index,"is",item)

ourverylonglist=[]

for i in range(0,100,1):
    ourverylonglist.append(i)

for i in ourverylonglist:
    print(i)
