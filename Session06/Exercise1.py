name=[]
age=[]
n=int(input("n="))
for i in range(n):
    p=input("Name=")
    a=int(input("Age="))
    name=name+[p]
    age=age+[a]
r1=zip(name,age)
r2=list(r1)
dic=dict(r2)
print(dic)
print(dic.keys())
print(dic.values())


