import numpy as np
d=np.array([[169,19,1],
            [175,32,0],
            [136,35,0],
            [174,65,1],
            [141,28,0],
            [176,15,1],
            [131,32,0],
            [166,6,1],
            [128,32,0],
            [179,10,1],
            [136,34,0],
            [186,2,1],
            [126,25,0],
            [176,28,0],
            [112,38,0],
            [169,9,1],
            [171,36,0],
            [116,25,0],
            [196,25,0]])
features=d[:,:2]
label=d[:,2]
from sklearn.linear_model import LogisticRegression
model1=LogisticRegression()
model1.fit(features,label)
logistic=model1.predict([[133,37]])
print("Logistic Prediction:",logistic)

from sklearn.neighbors import KNeighborsClassifier
model2=KNeighborsClassifier()
model2.fit(features,label)
neighbors=model2.predict([[133,37]])
print("KNN Prediction:",neighbors)

from sklearn.cluster import KMeans
model3=KMeans(n_clusters=2)
model3.fit(features)
KNN=model3.predict([[133,37]])
print(model3.labels_)
print("KNN Predict:",KNN)
