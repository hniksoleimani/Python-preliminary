import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("student_scores.csv")
print(data.shape)
print(data.describe())
data.plot(x='Hours',y='Scores',style='x')
plt.title("Hours versus percentage")
plt.xlabel("Hours Studied")
plt.ylabel("Percentage Score")
plt.show()
x=data.iloc[:,:-1].values
y=data.iloc[:,1].values
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(x,y,test_size=0.2)
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(xtrain,ytrain)
print(model.intercept_)   #arz az mabda moadele khati
print(model.coef_)          #shib moadele khati
ypred=model.predict(xtest)
d=pd.DataFrame({"ytest":ytest,"ypredict":ypred})
print(d)
from sklearn import metrics
print("Mean=",np.mean(y))
print("MAE",metrics.mean_absolute_error(ytest,ypred))
print("MSE",metrics.mean_squared_error(ytest,ypred))
print("RMSE",np.sqrt(metrics.mean_squared_error(ytest,ypred)))
print("+++++++++++++++++++++++++++++")
