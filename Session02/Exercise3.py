from math import *
def d(x1,y1,x2,y2):
    i=sqrt(((x2-x1)**2)+((y2-y1)**2))
    print("distance from (",x1,y1,") to (",x2,y2, ") equals",i)
    
x1=float(input("Enter x1 please:"))
y1=float(input("Enter y1 please:"))
x2=float(input("Enter x2 please:"))
y2=float(input("Enter y2 please:"))

d(x1,y1,x2,y2)
