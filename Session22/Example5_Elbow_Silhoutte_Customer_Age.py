import numpy as np
d=np.array([[15],[15],[16],[19],[19],[20],
                      [20],[21],[22],[28],[35],[40],
                      [41],[42],[43],[44],[60],[61],
                      [65]])
from sklearn.cluster import KMeans
se=[]
for i in range(1,10):
    model=KMeans(n_clusters=i,max_iter=300)
    model.fit(d)
    se.append(model.inertia_) #majmue morabaete favasel darune har khushe
import matplotlib.pyplot as plt
plt.plot(range(1,10),se)
plt.xlabel("Number of Clusters")
plt.ylabel("Se")
plt.title("Elbow")
plt.show()
"""
from sklearn.metrics import silhouette_score
sc=[]
for k in range(2,10):    #baraye ravesh silhouette range az 2 shoru mishe
    model2=KMeans(n_clusters=k,max_iter=300)
    model2.fit(d)
    score=silhouette_score(d,model2.labels_)  #data va label data
    sc.append(score)
plt.plot(range(2,10),sc)
plt.xlabel("Number of Clusters")
plt.ylabel("sc")
plt.title("Silhouette")

plt.show()
"""   

"""
model=KMeans(n_clusters=2,max_iter=300) #default number of iterations
model.fit(d)
labels=model.labels_
print(labels)
print(model.cluster_centers_)
"""
