import numpy as np
d=np.array([[120,50,1],
            [60,20,2],
            [145,65,1],
            [130,45,3],
            [50,15,2]])
from sklearn.cluster import DBSCAN
model=DBSCAN(eps=60,min_samples=2)
model.fit(d)
print(model.labels_)
print(model.fit_predict([[125,45,1]]))
#shoae behine dar dbscan ro chetor mohasebe konim? Search konam
