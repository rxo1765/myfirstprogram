"""
Ordinary Least Squares using OLS from statsmodel.api
predict point spread using line, and difference in days off
    the theory being more days off means a team is better rested
    and better prepared
    
y is the response variable; actual spread (homescore - visitscore)
x1 is the line
x2 is the difference in days off

y= b0 + b1*x1 + b2*x2
"""

import statsmodels.api as sm
import pandas as pd
import numpy as np

#reading data from the csv
data = pd.read_csv('NFL2022.csv')

# defining the varibales

y = (data['hScore'] - data['vScore']).tolist()
x1 = data['line'].tolist()
x2 = (data['hDoff'] - data['vDoff']).tolist()

A = np.array([x1,x2]).T
A.shape
A = sm.add_constant(A)
A.shape

model = sm.OLS(y,A)
results = model.fit()
results.params
results.tvaules

print(results.t_test([3,0]))

# adding the constant term
x = sm.add_constant(x)

# performing the regression