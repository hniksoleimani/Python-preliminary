import re
f1=open("a.txt","w+")
s1=['10','11','12','13','14','15','16','17','18','19','20']
f1.writelines(s1)
f1.close()
f2=open("a.txt","r+")
s2=f2.read(-1)
print(s2)
x=re.findall("\d.",s2)
print(len(x))
print(x)
sum=0
for i in range(len(x)):
    ss=int(x[i])
    sum+=ss
print("Mean equals:",sum/len(x))
