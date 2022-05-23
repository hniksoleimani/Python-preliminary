n=int(input("Number of tries="))
print("What is the most populous city in iran?")
f=0
print("------------------------------------")
for i in range(n):
    s=input("Answer=")
    s=s.upper()
    if s=="TEHRAN":
        print("Correct!")
        print("-----------------------------------------------")
        break
    else:
        print("Wrong answer.")
        f+=1
if f==(n):
    print("You Lose... :(")
else:
    print(" You won...!!!")
