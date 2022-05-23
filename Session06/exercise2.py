text1=input("Enter a text:")
set1={'hello', 'hi','salam','bye','goodbye'}
x=text1.split()
set2=set(x)
set3=set2.difference(set1)
lis=list(set3)
print(lis)
r=""
for i in range(0,len(lis)):
   r=r+" "+lis[i]
print(r)
