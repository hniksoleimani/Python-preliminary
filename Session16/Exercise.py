import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
data={"Physics":[18,12,19],
    "Chimistry":[16.25,15,20],
    "Mathematics":[14,13,18],
    "Literature":[17,15,17]}
y=pd.DataFrame(data,index=["Ali","Mohamad","Reza"])
print(y)
print(y.describe())
print(y.corr())
