import numpy as np
d=np.array([[15],[15],[16],[19],[19],[20],
                      [20],[21],[22],[28],[35],[40],
                      [41],[42],[43],[44],[60],[61],
                      [65]])
from sklearn.cluster import KMeans
model=KMeans(n_clusters=2,max_iter=300) #default number of iterations
model.fit(d)
labels=model.labels_    #Label har dade ya shomare daste ra moshakhas mikonad
print(labels)
print(model.cluster_centers_)

