import numpy as np
import sys

A = np.array([[1,2],
              [3,4]])

print(A)
type(A)
A.shape

'''
system of equations:
  suppose x1 =5, and x2 =1 then
  1*x1 + 2*x2 = 7
  3*x1 + 4*x2 = 19

A@x = b
A.inv @ A @x =  A.inv @ b
'''

b =np.array([ [7],
             [19]])
print(f"\nb = {b}")

## solve equations

detA = np.linalg.det(A)
print (f"determinant of matrix A is {detA: 0.3f}")

Ainv = np.linalg.inv(A)
print(f"\nA- inverse = \n{Ainv}")

print (f"\n Ainv @ A is {Ainv @ A}")

x = Ainv @ b
print(f"\nunknowns are: \n{x}")

# check
print(f"\ncheck: \n{A@x}")



