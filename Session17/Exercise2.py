import numpy as np
from scipy.optimize import curve_fit
import matplotlib.pyplot as plt
def f(x,a,w,phi):
    return a*(np.sin(w*x+phi))
x=np.linspace(-5,5,500)
y=f(x,a=2.9,w=1.5,phi=100)
yi=y+0.4*np.random.normal(size=len(x))
popt,pcov=curve_fit(f,x,yi)
a,w,phi=popt
print(a,w,phi)
y_fit=f(x,a,w,phi)
plt.plot(x,yi,"*",label="Data")
plt.plot(x,y_fit,label="Fit")
plt.legend()

plt.show()

