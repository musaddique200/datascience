import numpy as np

# Step 1: Define a square matrix A
A = np.array([[4, -2],
              [1,  1]])

# Step 2: Diagonalize the matrix A (A = P D P^-1)
# Calculate eigenvalues (D) and eigenvectors (P)
eigenvalues, eigenvectors = np.linalg.eig(A)

# Step 3: Diagonal matrix D (containing the eigenvalues)
D = np.diag(eigenvalues)

# Step 4: Matrix P (containing the eigenvectors as columns)
P = eigenvectors

# Step 5: Compute the inverse of P
P_inv = np.linalg.inv(P)

# Step 6: Inverse of the diagonal matrix D
D_inv = np.diag(1 / eigenvalues)

# Display the results
print("Original Matrix A:")
print(A)
print("\nDiagonal Matrix D (Eigenvalues):")
print(D)
print("\nMatrix P (Eigenvectors):")
print(P)
print("\nInverse of P:")
print(P_inv)
print("\nInverse of the Diagonal Matrix D:")
print(D_inv)

