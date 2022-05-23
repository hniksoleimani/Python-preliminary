x=[[19.5,3,1,3],
     [16.5,0,1,4],
     [15,0,0,3],
     [17,2,1,2.5],
     [18.5,2,0,2.5],
     [15.5,1,1,2.5],
     [19,3,1,3]]
y=[1,0,0,1,1,0,1]
from sklearn.tree import DecisionTreeClassifier
model=DecisionTreeClassifier()
model.fit(x,y)
print(model.predict([[15.5,5,0,3]]))
