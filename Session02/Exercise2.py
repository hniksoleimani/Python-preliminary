def multi(i):
    if(i%2)==0 and (i%7)==0:
        print(i,"is a multiple of both 2 and 7")
    elif (i%2)==0:
        print(i,"is a multiple of 2")
    elif(i%7)==0:
        print(i,"is a multiple of 7")
    else:
        print(i,"is neither a multiple of 2 nor 7")
    
i=int(input("Enter an number please:"))
multi(i)
