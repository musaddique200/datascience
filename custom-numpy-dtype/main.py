import numpy as np

# I created a custom NumPy data type with fields for 'Name', 'Age', and 'Score'.
custom_dtype = np.dtype([
    ('Name', 'U10'),   # String field (max 10 characters)
    ('Age', 'i4'),     # Integer field (4-byte integer)
    ('Score', 'f4')    # Float field (4-byte float)
])

# Now I’m creating a NumPy array using this custom data type.
data = np.array([
    ('Alice', 25, 85.5),
    ('Bob', 30, 90.0),
    ('Charlie', 35, 78.2)
], dtype=custom_dtype)

print("Custom NumPy Array:")
print(data)

# Accessing fields for demonstration
print("\nNames in the array:", data['Name'])
print("Ages in the array:", data['Age'])
print("Scores in the array:", data['Score'])

