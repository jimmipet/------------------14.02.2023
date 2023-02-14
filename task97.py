import numpy as np
A = np.array([[1+2j, 1-2j], [-1+2j, -1+2j]])
b = np.array([12, 15])
x = np.linalg.solve(A, b)
print("x =", x[0])
print("y =", x[1])
