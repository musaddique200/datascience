# Here's my 2D array.
array_2d = np.array([[1, 2, 3],
                     [4, 5, 6],
                     [7, 8, 9]])

# I need to find the sum of each row.
row_sums = array_2d.sum(axis=1, keepdims=True)

# Now, I divide each element by its row's sum to normalize.
normalized_array = array_2d / row_sums

# Let's see the result!
print("Normalized array:")
print(normalized_array)
