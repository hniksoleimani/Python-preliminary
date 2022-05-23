import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(x,a,b):
    return 1/(a+b*x)
x=np.array([-5,-2,-1,-.1,-.01-.001,-.0001,.0001,.001,.01,.1,1,2,5])
y=f(x,a=2,b=5)
yi=y+0.15*np.random.normal(size=len(x))
popt,pcov=curve_fit(f,x,yi)
a,b=popt
print(a,b)
y_fit=f(x,a,b)
plt.plot(x,yi,color="red",label="Data")
plt.plot(x,y_fit,label="Fit")
plt.legend()

plt.show()


