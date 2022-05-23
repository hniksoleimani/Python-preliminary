import pandas as pd
c = {'home': [1,0,1,1,0,0],
'year': [3,1,1.5,5,2,3.5],
'loan': [1,0,1,1,0,0]
}
d=pd.DataFrame(c)
x=d[["home","year"]]
y=d['loan']

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
scaler.fit(d.drop("loan",axis=1))
x_scaled=scaler.transform(d.drop("loan",axis=1))
xtest=x
xtrain=x
ytrain=y
ytest=y
from sklearn.neighbors import KNeighborsClassifier
import numpy as np
"""
error=[]

for i in range(1,6):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(xtrain,ytrain)
    ypred=model.predict(xtest)
    d2=pd.DataFrame({"ytest":ytest,"ypred":ypred})
    error.append(np.mean(ypred!=ytest))
    
print(error)
  
import matplotlib.pyplot as plt
plt.plot(range(1,6),error)
plt.xlabel("n_neighbors")
plt.ylabel("error")
plt.legend()
plt.show()
"""
model=KNeighborsClassifier(n_neighbors=1)
model.fit(xtrain,ytrain)
ypred1=model.predict([[1,2.5]])
ypred2=model.predict([[0,2]])
print(ypred1)
print(ypred2)

