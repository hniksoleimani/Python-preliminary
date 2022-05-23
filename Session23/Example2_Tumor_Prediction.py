import numpy as np
d=np.array([[23,5,0],
            [25,10,0],
            [23,15,1],
            [17,5,0],
            [35,5,1],
            [19,10,0],
            [30,15,1],
            [35,15,1],
            [40,10,1],
            [20,5,0],
            [25,5,0],
            [30,5,1],
            [15,10,0],
            [45,15,1],
            [43,15,1],
            [15,10,1],
            [20,10,0],
            [40,10,1]
            ])
features=d[:,:2]
label=d[:,2]
from sklearn.linear_model import LogisticRegression
model1=LogisticRegression()
model1.fit(features,label)
logistic=model1.predict([[28,5]])
print("Logistic Prediction:",logistic)

from sklearn.neighbors import KNeighborsClassifier
model2=KNeighborsClassifier()
model2.fit(features,label)
neighbors=model2.predict([[28,5]])
print("KNN Prediction:",neighbors)

from sklearn.cluster import KMeans
model3=KMeans(n_clusters=2)
model3.fit(features)
KNN=model3.predict([[28,5]])
print(model3.labels_)
print("KNN Predict:",KNN)
