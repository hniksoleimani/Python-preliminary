import pandas as pd
c = {'gmat': [780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
'admitted': [1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]
}
d=pd.DataFrame(c)
x=d[["gmat","gpa","work_experience"]]
y=d["admitted"]
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.25,random_state=0)
model=LogisticRegression()
model.fit(x_train,y_train)

#Prediction:
ypred=model.predict(x_test)
print(x_test)
print("=============================")
d2=pd.DataFrame({"ytest":y_test,"ypred":ypred})
print(d2)



#Precision&Accuracy
from sklearn.metrics import confusion_matrix,classification_report
print(confusion_matrix(y_test,ypred))
print("X==============================X")
print(classification_report(y_test,ypred))
