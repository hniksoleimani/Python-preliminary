r=[]
employee=int(input("Enter number of employees:"))
for i in range(employee):
    extra=0
    hours=0
    salary=0
    l=i+1
    print("Enter worker ID for employee no",l,":")
    id=int(input(" "))
    print("Enter working hours for employee no",l,":")
    hours=int(input(""))
    if hours>160:
        extra=hours-160
        hours=160
        if extra>40:
            extra=40
    salary=(hours*100000)+(extra*50000)
    v=[(l,id,hours,extra,salary)]
    r=r+v
    print("Salary for employee no",l,"is=",salary)
print(r)
