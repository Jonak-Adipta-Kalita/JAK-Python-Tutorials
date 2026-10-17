import numpy as np

arr = np.array([[1, 2, "3"], [4, 5, 6], ["7", 8, 9]], dtype=np.int32)

print(f"Array: {arr}")

print(f"Shape: {arr.shape}")
print(f"At [0, 2]: {arr[0, 2]}")

print(f"NDim: {arr.ndim}")
print(f"Shape: {arr.shape}")
print(f"DType: {arr.dtype}")

print(f"Accessing Rows for Col 1: {arr[:, 1]}")

print("\nSpecial Values:")
print(np.nan)
print(np.inf)
