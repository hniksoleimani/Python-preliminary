reserved=[]
rooms=["A","B","C"]
n=1
while n<1080:
    room=input("Enter room class[A, B or C]:")
    r=room.upper()
    if r not in rooms:
        print("Wrong room class.")
        continue
    bed=int(input("Enter number of bedrooms[1-3]:"))
    date=int(input("Enter date[1-30]:"))
    days=int(input("Enter number of days spending:"))
    book=date+time
    if book >30
    book=book-30
    if date<1 or date>30 or time<9 or time>20:
        print("Wrong date or time.")
        continue
    l=[(r,date,time)]
    s=[l]
    if l in reserved:
        print("Room booked during that time.:")
        continue
    else:
        name=input("Enter your name:")
        last=input("Enter your last name:")
        print(name,last,"booked room",r,"on",date,"th at",time,"o` clock")
        n+=1
        reserved+=s
        print("------------------------------------------------------")
        print(reserved)
        print(l)
        print(s)
