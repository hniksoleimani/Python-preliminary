import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import trapz,simpson,quad,odeint
def f(u,x):
    return [u[1],np.cos(2*x)-2*u[1]-2*u[0]]
u0=[0,0]
x=np.linspace(0,10,100)
us=odeint(f,u0,x)
y=us[:,0]
print(us)
plt.plot(x,y)
plt.show()
