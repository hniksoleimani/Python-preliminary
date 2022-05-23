import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize
def f(x):
    return x**2+x+2
mimin=minimize(f,0,method='BFGS')
print(mimin)
