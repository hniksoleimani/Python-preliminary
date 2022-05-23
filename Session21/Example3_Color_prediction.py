import numpy as np
import pandas as pd
data=np.array([[120,50,1,"A"],[60,20,2,"B"],[145,65,1,"A"],[130,45,3,"A"],[50,15,2,"B"]])
features=data[:,:3]
label=data[:,3]
from sklearn.neighbors import KNeighborsClassifier
model1=KNeighborsClassifier(n_neighbors=3)
model1.fit(features,label)
sample=[[125,45,1]]
pred1=model1.predict(sample)
print(pred1)
from sklearn.linear_model import LogisticRegression
model2=LogisticRegression()
model2.fit(features,label)
pred2=model2.predict(sample)
print(pred2)
