#Dictionaries.py
#Matthew Raines, COP2500

#dictionary["name"] Gives the value for that item.


#Add item to the dictionary.

def add_item(dictionary):
    newItem=input("Enter dictionary item with format 'name,value': ")
    newItemList=newItem.split(",")
    newItemName=newItemList[0]
    newItemValue=newItemList[1]
    dictionary[newItemName] = newItemValue

    print("Entry added.")


#Remove item from dictionary given name.

def remove_item(dictionary):
    removeItemName=input("What is the name of the item you want to remove? ")
    if removeItemName in dictionary:
        dictionary.pop(removeItemName)
        print("Item removed.")
    else:
        print("Item doesn't exist.")

    
#Lists each item in the dictionary.

def list_items(dictionary):
    for name in dictionary:
        print(name,":", dictionary[name])


#Looks up item in dictionary given name.

def look_up_item(dictionary):
    lookupItemName=input("What item do you want to look up? ")

    if lookupItemName in dictionary:
        print(lookupItemName,":",dictionary[lookupItemName])




dictionary={}

while True:
    response=input("Do you want to add, remove, list, or lookup? ")

    if response=="add":
        add_item(dictionary)
    elif response=="remove":
        remove_item(dictionary)
    elif response=="list":
        list_items(dictionary)
    elif response=="lookup":
        look_up_item(dictionary)
    elif response=="exit":
        break

