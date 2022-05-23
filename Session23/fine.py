import numpy as np
import pandas as pd
crime={"State":["Albama","Alaska","Arizona","Arkansas","California","Colorado","Connecticut","Delaware","Florida","Georgia","Hawaii","Idaho","Illinois","Indiana","Iowa"],                                 
            "Murder":[13.2,10.0,8.1,8.8,9.0,7.9,3.3,5.9,15.4,17.4,5.3,2.6,10.4,7.2,2.2],
            "Assualt":[236,263,294,190,276,204,110,238,335,211,46,120,249,113,56],
            "Urbanpop":[58,48,80,50,91,78,77,72,80,60,83,54,83,65,57],
            "Rape":[21.2,44.5,31.0,19.5,40.6,38.7,11.1,15.8,31.9,25.8,20.2,14.2,24.0,21.0,11.3]}
c=pd.DataFrame(crime)

print(c)
