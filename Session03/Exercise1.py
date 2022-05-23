from math import *
num=int(input("Enter a number:"))
j=1
s=0
for i in range(1,num+1):
    s=s+(j**2)
    j+=1
print("Sum of squares equals:",s)
print("Square root of the sums equals:", sqrt(s))
    
