import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
data=pd.read_excel("T_shirt.xlsx")
print(data)
print(data.shape)
print(data.describe())
x=data[["Height","Weight"]]
y=data["T-Shirt Size"]

data.plot(x='Height',y='Weight',style='x')
plt.title("Height vs Weight")
plt.xlabel("Height")
plt.ylabel("Weight")
plt.show()
x=data.iloc[:,:-1].values
y=data.iloc[:,2].values
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LogisticRegression
model1=LogisticRegression()
model1.fit(xtrain,ytrain)
print(model1.intercept_)   #arz az mabda
print(model1.coef_)          #shib
y1=model1.predict([[169,69]])
print(y1)
"""
#finding thee best neighbor
error=[]
for i in range(1,15):
    model=KNeighborsClassifier(n_neighbors=i)
    model.fit(xtrain,ytrain)
    ypred=model.predict(xtest)
    error.append(np.mean(ypred!=ytest))

plt.plot(range(1,15),error)
plt.xlabel("n_neighbors")
plt.ylabel("error")
plt.show()

"""
model=KNeighborsClassifier(n_neighbors=1)
model.fit(xtrain,ytrain)
ypred=model.predict([[169,69]])
print(ypred)
"""
d=pd.DataFrame({"ytest":ytest,"ypredict":ypred})
print(d)
from sklearn import metrics
print("Mean=",np.mean(y))
print("MAE",metrics.mean_absolute_error(ytest,ypred))
print("MSE",metrics.mean_squared_error(ytest,ypred))
print("RMSE",np.sqrt(metrics.mean_squared_error(ytest,ypred)))
print("+++++++++++++++++++++++++++++")

"""
