r=[]
n=0
while n<360:
    print("r=",r)
    date=input("date:[1-30]=")
    time= input("time:[9-20]=")
    p=date+ " "+time
    date=int(date)
    time=int(time)
    if date<1 or date>30 or time <9 or time >20:
         print("wrong,try again")
         continue
    if p in r:
         print("date taken")
         print("---------------------------------------------")
         continue
    else:
         print("Enter info:")
         name=input("First name:")
         last=input("Last name:")
         print(name,last,"booked",date,"th at", time,"o`clock")
         r=r+[p]
         n+=1
         print("-----------------------------------------------")
