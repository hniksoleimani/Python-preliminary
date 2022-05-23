import numpy as np
import pandas as pd
d=pd.read_csv("Wholesale customers data.csv")
#print(d)
from sklearn.preprocessing import MinMaxScaler
mms=MinMaxScaler()
mms.fit(d)
d1=mms.transform(d)
from sklearn.cluster import KMeans
ssd=[]
for i in range(1,15):
    model=KMeans(n_clusters=i)
    model.fit(d1)
    ssd.append(model.inertia_)

import matplotlib.pyplot as plt
plt.plot(range(1,15),ssd)
plt.xlabel("Number of Clusters")
plt.ylabel("ssd")
plt.show()


#Silouette anjam shavad
