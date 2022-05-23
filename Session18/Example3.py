import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz,simpson,quad,odeint
def f(x,y):
    dydx=0.3*y
    return dydx
x=np.linspace(0,20,40)
y0=5
y=odeint(f,y0,x)
plt.plot(x,y)
plt.xlabel("Time")
plt.ylabel("Y(x)")
plt.legend()
plt.show()

