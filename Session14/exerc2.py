from matplotlib import pyplot as plt
import numpy as np
a=np.array([3,2,-1])
p=np.poly1d(a)
r=np.roots(p)
print("Polynomial:",p)
print("Roots are:",r)
f=np.polyval(a,-2)
print("Value of function at point (-2):",f)
d=np.polyder(p,1)
print("First derivative of the polynomial:",d)
print("Value of derivative at point(-2):",d(-2))
