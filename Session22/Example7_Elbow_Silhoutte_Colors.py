import numpy as np
import matplotlib.pyplot as plt
d=np.array([[120,50,1],
                   [60,20,2],
                   [145,65,1],
                   [130,45,3],
                   [50,15,2],])
print(d)
"""
se=[]
from sklearn.cluster import KMeans
for i in range(1,5):
    model1=KMeans(n_clusters=i,max_iter=300) #default number of iterations
    model1.fit(d)
    se.append(model1.inertia_)
plt.plot(range(1,5),se)
plt.xlabel=("Number of Clusters")
plt.ylabel=("se")
plt.title("Elbow")
plt.show()
"""
from sklearn.cluster import KMeans

from sklearn.metrics import silhouette_score
sc=[]
for k in range(2,5):    #baraye ravesh silhouette range az 2 shoru mishe
    model2=KMeans(n_clusters=k,max_iter=300)
    model2.fit(d)
    score=silhouette_score(d,model2.labels_)  #data va label data
    sc.append(score)
plt.plot(range(2,5),sc)
plt.xlabel("Number of Clusters")
plt.ylabel("sc")
plt.title("Silhouette")
plt.show()

