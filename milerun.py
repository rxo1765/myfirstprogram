# -*- coding: utf-8 -*-
"""
Created on Thu Jul 27 17:38:42 2023

@author: be
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from os import chdir
from scipy.optimize import minimize

chdir("C:/Users/be/Downloads/mileR")
dataRUN =pd.read_csv("mileRecords.csv")

x = np.array(dataRUN["year"])
x = x-x[0]
y = np.array(dataRUN["time"])

plt.plot(x,y,'xk')
plt.xlabel('Year')
plt.ylabel('Time in Seconds')
plt.title('Mile Record Time')

def fmin(param):
    K=param[0]
    r=param[1]
    e=y-r*y*(1-y/K)*x
    return(np.dot(e,e.T))

x0=(3.1,-.25)
opt=minimize(fmin,x0)
print(opt)
print(opt.x[0])