import pandas as pd
c = {'gmat': [780,750,690,710,680,730,690,720,740,690,610,690,710,680,770,610,580,650,540,590,620,600,550,550,570,670,660,580,650,660,640,620,660,660,680,650,670,580,590,690],
'gpa': [4,3.9,3.3,3.7,3.9,3.7,2.3,3.3,3.3,1.7,2.7,3.7,3.7,3.3,3.3,3,2.7,3.7,2.7,2.3,3.3,2,2.3,2.7,3,3.3,3.7,2.3,3.7,3.3,3,2.7,4,3.3,3.3,2.3,2.7,3.3,1.7,3.7],
'work_experience': [3,4,3,5,4,6,1,4,5,1,3,5,6,4,3,1,4,6,2,3,2,1,4,1,2,6,4,2,6,5,1,2,4,6,5,1,2,1,4,5],
'admitted': [1,1,0,1,0,1,0,1,1,0,0,1,1,0,1,0,0,1,0,0,1,0,0,0,0,1,1,0,1,1,0,0,1,1,1,0,0,0,0,1]}
d=pd.DataFrame(c)
print(d)
features=d[["gmat","gpa","work_experience"]]
label=d["admitted"]
#print(label)
from sklearn.model_selection import train_test_split
xtrain,xtest,ytrain,ytest=train_test_split(features,label,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier
model=RandomForestClassifier(n_estimators=50)
model.fit(xtrain,ytrain)
ypred=model.predict(xtest)
l={"ytest":ytest,"ypred":ypred}
df2=pd.DataFrame(l)
print(df2)
from sklearn.metrics import classification_report,confusion_matrix,accuracy_score
result1=confusion_matrix(ytest,ypred)
print("confusion_matrix:",result1)
result2=classification_report(ytest,ypred)
print("classification_report:",result2)
result3=accuracy_score(ytest,ypred)
print("Accuracy:",result3)


#Random Forest is a Supervised Learning Method.
#Dataset is divied into a number of random samples.
#Each sample is calculated separately using Decision Tree


