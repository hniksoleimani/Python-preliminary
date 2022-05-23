from math import *
def Eqn(a,b,c):
    d=((b**2)-(4*a*c))
    if d<0:
        print(" The equation does not have any real roots.")
    elif d==0:
        x=((-b)/(2*a))
        print(" The equation has one real root which is:",x)
    elif d>0:
        x1=(((-b)+sqrt(d))/(2*a))
        x2=(((-b)-sqrt(d))/(2*a))
        print(" The roots are:",x1,x2)

a=float(input("Enter a:"))
b=float(input("Enter b:"))
c=float(input("Enter c:"))
Eqn(a,b,c)
