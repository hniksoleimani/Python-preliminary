from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
def f(x):
    return np.array([10*(x[1]-x[0]**2),(1-x[0])])
input=np.array([2,2])
res=least_squares(f,input)
print(res)
