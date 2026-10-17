import numpy as np

l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 0]

a1 = np.array(l1)
a2 = np.array(l2)

print("Scalar Multiplication:")
print(l1 * 5)
print(a1 * 5)
print()

print("Scalar Addition:")
print(l1 + l2)
print(a1 + a2)
print()

# If you call a np.math_function, it will work on the whole array. Example:
print(np.sqrt(a1))
print()

a1 = np.append(a1, a2)
print(f"Appended a1 to a2: {a1}")

print()
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(a.shape)

print("\nreshaping to (3, 4):")
# use arr.reshape(), which returns the reshaped array
print(a.reshape(3, 4))
# or, you can use arr.resize(), which changes original array
a.resize(4, 3)
print(a)

print("\nflattening")
# use arr.flatten() or arr.ravel(), but ravel returns a pointered object to the original array, so any changes to the new variable reflects onto the original
print(a.ravel())
print(a.flatten())

print("\nTransposing")
# use arr.T or arr.transpose()
print(a.T)
print(a.transpose())
