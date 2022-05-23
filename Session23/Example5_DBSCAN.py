import numpy as np
d=np.array([[7,3],
            [7,4],
            [8,3],
            [9,3],
            [5,2],
            [4,3],
            [3,4]])
from sklearn.cluster import DBSCAN
model=DBSCAN(eps=2,min_samples=2)
model.fit(d)
print(model.labels_)
print(model.fit_predict([[8,4]]))
