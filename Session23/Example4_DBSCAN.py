import numpy as np
d=np.array([[1,2],
            [2,2],
            [2,3],
            [8,7],
            [8,8],
            [25,80]])
from sklearn.cluster import DBSCAN
model=DBSCAN(eps=3,min_samples=2)
model.fit(d)
print(model.labels_)
#-1 dade hae part hastan
