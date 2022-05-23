from scipy.optimize import curve_fit
import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import least_squares
from datetime import datetime
a=datetime.now()
for i in range(10000):
    b=datetime.now()
    c=b-a
    d=c.total_seconds()
    if d<10:
        print(i)

print("a=",a)
print("b=",b)
print("c=",c)
print("d=",d)
