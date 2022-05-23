import numpy as np
x=np.array([0,2,4,5,7,9,15,20,22])
y=np.array([-3,-1,4,3,5,9,5,6,7])
from scipy.optimize import curve_fit
def f(x,a1,a2,a3,a4):
    return a1+a2*x+a3*x**2+a4*x**3
popt,pocv=curve_fit(f,x,y)
a1,a2,a3,a4=popt
ypred=f(x,a1,a2,a3,a4)
import matplotlib.pyplot as plt
plt.plot(x,y,"o")
plt.plot(x,ypred)
from sklearn.metrics import r2_score
print("r2=",r2_score(y,ypred))
plt.show()
