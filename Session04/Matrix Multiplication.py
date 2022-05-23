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
        for k in range(len(Y[0])):
            R[i][j]=R[i][j]+(X[i][k]*Y[k][j])
      
for l in R:
    print(l)

