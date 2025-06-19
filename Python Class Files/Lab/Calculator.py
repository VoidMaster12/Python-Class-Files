#Calculator.py - Calculations in Python
#Matthew Raines, COP2500

x= float(input("Enter a value for x: "))
y= float(input("Enter a value for y: "))

op=input("Enter desired operation: ")

if (op =="add"):
    z = x+y
elif (op == "subtract"):
    z = x-y
elif (op == "multiply"):
    z = x*y
elif (op == "divide"):
    z = x/y
else:
    z = "Invalid operation."

print(f"The result is: {z}")
