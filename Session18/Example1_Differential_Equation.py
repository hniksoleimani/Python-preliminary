import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz,simpson,quad,odeint
def f(y,x):
    dydx=x-y
    return dydx
x=np.linspace(0,5,40)
y0=1
y=odeint(f,y0,x)
plt.plot(x,y)
plt.show()


