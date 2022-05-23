import numpy as np
from sklearn import linear_model
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
model=linear_model.LinearRegression()
x=np.array([0,2,4,5,7,9,15,20,22])
y=np.array([-3,-1,4,3,5,9,5,6,7])
X=x[:,np.newaxis]
model.fit(X,y)
ypred=model.predict(X)
plt.plot(x,y,"x")
plt.plot(X,ypred)
plt.show()
print("r2=",r2_score(y,ypred))
