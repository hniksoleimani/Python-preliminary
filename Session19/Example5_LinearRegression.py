import pandas as pd
df=pd.read_excel("car.xlsx")
x=df[["Volume", "Weight"]]
y=df["CO2"]
from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(x,y)
co2pred=model.predict([[1300,2300]])
print(co2pred)
print(model.coef_)



#co2pred.model.predict(x)
#from sklearn.metrics import r2_score
#print("r2=",r2_score(y,co2pred"""ypred""")))
