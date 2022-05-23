from math import *
def Grade(a):
    if (a>=0) and (a<10):
        print(" This student has failed.")
    elif (a>=10) and (a<15):
        print(" This student did good")
    elif (a>=15) and (a<18):
        print(" This student did a very good job!")
    elif (a>=18) and (a<=20):
        print(" This student did an excellent job!.")
    else:
        print("Invalid grade.")
        

a=float(input("Enter Strudent`s grade:"))
Grade(a)
