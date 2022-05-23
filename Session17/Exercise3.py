import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(x,a,b,c):
    return (a*(np.power(x,b)))+c
x=np.linspace(0,4,50)
y=f(x,a=3,b=2,c=0.5)
yi=y+0.2*np.random.normal(size=len(x))
popt,pcov=curve_fit(f,x,yi)
a,b,c=popt
print(a,b,c)
y_fit=f(x,a,b,c)
plt.plot(x,yi,"x",label="Data")
plt.plot(x,y_fit,label="Fit")
plt.legend()
plt.show()

