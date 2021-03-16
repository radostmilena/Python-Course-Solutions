from scipy import linalg
import numpy as np

#a. Define a matrix A
A = np.arange(1, 10, 1).reshape((3,3))
print(A)

#b. Define a vector b
B = np.arange(1, 4, 1)
print(B)

#c. Solve the linear system of equations A x = b
p, res, rnk, s = linalg.lstsq(A,B)
print(p)

#d. Check that your solution is correct by plugging it into the equation
B_check = np.dot(A, p)
print(B_check)

#e. Repeat steps a-d using a random 3x3 matrix B (instead of the vector b)
B = np.random.rand(9).reshape((3,3))
p, res, rnk, s = linalg.lstsq(A,B)
B_check = np.dot(A, p)
print(B_check)

#f. Solve the eigenvalue problem for the matrix A and print the eigenvalues and eigenvectors
eigval, eigvec = linalg.eig(A)
print(eigval)
print(eigvec)

#g. Calculate the inverse, determinant of A
inv_A = linalg.inv(B)
print(inv_A)
inv_det_A = linalg.det(inv_A)
print(inv_det_A)

#h. Calculate the norm of A with different orders
linalg.norm(A, 2)
linalg.norm(A, -2)
linalg.norm(A, -np.inf)
linalg.norm(A, np.inf)
