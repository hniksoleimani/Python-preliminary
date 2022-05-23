r=[]
n=0
while n<31:
    print("r=",r)
    date=int(input("date:[1-30]="))
    if date<1 or date>30:
         print("wrong,try again")
         continue
    if date in r:
         print("date taken")
         print("---------------------------------------------")
         continue
    else:
         print("Enter info:")
         name=input("First name:")
         last=input("Last name:")
         print(name,last,"booked",date)
         r=r+[date]
         n+=1
         print("-----------------------------------------------")
