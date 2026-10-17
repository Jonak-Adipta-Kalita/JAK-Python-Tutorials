import numpy as np

a1 = np.array([[1, 2, 3, 4, 5, 6], [7, 8, 9, 10, 11, 12]])
a2 = np.array([[13, 14, 15, 16, 17, 18], [19, 20, 21, 22, 23, 24]])

a = np.concatenate((a1, a2), axis=0)  # Row Wise appending
b = np.concatenate((a1, a2), axis=1)  # Col Wise appending

c = np.stack((a1, a2))  # Creates new dimensions

d = np.vstack((a1, a2))  # Row wise appending
e = np.hstack((a1, a2))  # Col wise appending

print(a)
print()
print(b)
print()
print(c)
print()
print(d)
print()
print(e)

print("\nSplitting array:")
print(np.split(a, 2, axis=0))
print(np.split(a, 2, axis=1))
