ticket=0
r1=[]
code=[]
fine=[1000,1500,1700,1850,2000,2200,2300,2400,2500,3000]
for i in range(10):
    print("Driving offense code",fine.index(fine[i]),"pays",fine[i],"$ fine.")
for i in range(1000):
    n=int(input("Enter number of offenses:"))
    for i in range(n):
        m=int(input("Enter fine code[0-9]:"))
        ticket=ticket+fine[m]
        code=code+[(m)]
    name=input("Enter driver name:")
    last=input("Enter driver`s last name:")
    lic=input("Enter car`s license plate number:")
    r=[name,last,code,lic,ticket]
    r1=r1+[(r)]
    code=[]
    ticket=0
    print(r1)
