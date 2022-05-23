import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(x,a,b):
    return a*(np.sin(b*x))
x=np.linspace(-5,5,50)
y=f(x,a=2.9,b=1.5)
yi=y+0.4*np.random.normal(size=len(x))
popt,pcov=curve_fit(f,x,yi)
a,b=popt
print(a,b)
y_fit=f(x,a,b)
plt.plot(x,yi,"*",label="Data")
plt.plot(x,y_fit,label="Fit")
plt.legend()

plt.show()
