import numpy as np
d=np.array([[120,50,1],
                   [60,20,2],
                   [145,65,1],
                   [130,45,3],
                   [50,15,2],])
print(d)

from sklearn.cluster import KMeans
model=KMeans(n_clusters=2,max_iter=300) #default number of iterations
model.fit(d)
labels=model.labels_
print(labels)
print(model.cluster_centers_)

j=model.predict([[125,45,1]])
print(j)


