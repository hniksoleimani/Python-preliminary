import pandas as pd
c = {'Size': [60,80,40,75,90,35,50,80,100,50],
       'Number_of_Rooms': [2,2,1,2,3,1,1,2,3,1],
       'Floor': [4,2,11,2,4,1,3,5,4,1],
       'Age':[10,5,15,5,10,2,10,5,10,2],
       'Region':[1,1,1,2,2,2,2,3,3,3],
       'Price':[620,920,360,1125,1170,560,700,1600,1800,1000]
}
d=pd.DataFrame(c)
features=d[["Size","Number_of_Rooms","Floor","Age","Region"]]
label=d["Price"]
from sklearn.neighbors import KNeighborsClassifier
model=KNeighborsClassifier(n_neighbors=2)
model.fit(features,label)
ypred1=model.predict([[170,1,2,5,2]])
print(ypred1)
ypred2=model.predict([[80,2,5,5,3]])
print(ypred2)
#Not a very good method, model 2 is from dataset yet it is not predicted right.
