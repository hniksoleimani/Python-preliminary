import numpy as np
d=np.array([[7,3],
                   [7,4],
                   [8,3],
                   [9,3],
                   [5,2],
                   [4,3],
                   [3,4]])
print(d)
from sklearn.cluster import KMeans
model=KMeans(n_clusters=7,max_iter=300) #default number of iterations
model.fit(d)
labels=model.labels_
print(labels)
print(model.cluster_centers_)

   
