from scipy.interpolate import interp1d
import numpy as np
from matplotlib import pyplot
x=np.array([0,1,2,3,4,5,6,7,8,9])
y=np.array([1,2.84,5.9,10.14,16.24,25.04,36.72,50.65,65.98,82.41])
f=interp1d(x,y,kind="linear")
xnew=np.arange(0,9.1,0.1)
ynew=f(xnew)
print(ynew)
pyplot.plot(x,y,"o")
pyplot.plot(xnew,ynew,"-")
pyplot.show()

