#lakearea.ya - Calculate area
#Matthew Raines, COP2500

#This file was created to calculate the area of a half-circular lake
#given the radius of the lake in meters.
r=int(input("What is the radius of the lake in meters? "))

pi=3.1416
a=(pi*r**2)/2

print("The area of the lake is",a,"m^2")
