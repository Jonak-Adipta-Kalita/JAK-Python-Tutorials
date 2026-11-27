import numpy as np

A = np.array([[3, 1, 1], [1, 2, 1], [1, 1, 3]])
B = np.array([11, 10, 13])

A_inv = np.linalg.inv(A)

x, y, z = A_inv @ B

print(A_inv)
print(x, y, z)
