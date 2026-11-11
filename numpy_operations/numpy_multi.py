""" import numpy as np
A=np.array([1,4,6])
B=np.array([[5,9,3],[8,4,2]])
print(A*B) 
"""

import numpy as np

A = np.array([[1, 2],
              [3, 4]])

B = np.array([[5, 6],
              [7, 8]])

print("Element-wise multiplication:")
print(A * B)

print("Matrix multiplication:")
print(A @ B)

print("Using NumPy function:")
print(np.matmul(A, B))