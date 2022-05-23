X=[[1,7,3],
    [4,8,6],
    [7,5,9]]
Y=[[1,8,1],
    [6,2,3],
    [4,5,3]]
R=[[0,0,0],
    [0,0,0],
    [0,0,0]]
Xt=[[0,0,0],
    [0,0,0],
    [0,0,0]]
for i in range(len(X)):
    for j in range(len(X[0])):
        R[i][j]=X[0][i]*Y[j][0]
        #Xt[j][i]=X[i][j]
for l in R:
    print(l)
#for x in Xt:
#    print(x)
#print(X[0][0],X[1][0],X[2][0])
