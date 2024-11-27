import numpy as np

array_2d = np.array([[1,2,3],
                     [4,5,6],
                     [7,8,9]])

row_sums = array_2d.sum(axis=1, keepdims=True)

normalized_array = array_2d / row_sums

print("Normalized array:")
print(normalized_array)
