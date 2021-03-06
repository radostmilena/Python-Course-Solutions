#!/usr/bin/python3 

import numpy as np

#a. Create a null vector of size 10 but the fifth value which is 1
zeros = np.zeros(10)
zeros[5] = 1
print(zeros)

#b. Create a vector with values ranging from 10 to 49
vector = np.arange(10, 50, 1)
print(vector)

#c. Reverse a vector (first element becomes last)
rev_vector = vector[::-1]
print(rev_vector)

#d. Create a 3x3 matrix with values ranging from 0 to 8
matrix = np.arange(9).reshape((3, 3))
print(matrix)
matrix = np.random.randint(0, 8, 9).reshape((3, 3))
print(matrix)

#e. Find indices of non-zero elements from [1,2,0,0,4,0]
some_vector = [1, 2, 0, 0, 4, 0]
indices = np.where(some_vector)
print(indices)

#f. Create a random vector of size 30 and find the mean value
r = np.random.rand(30)
av = np.average(r)
print(av)

#g. Create a 2d array with 1 on the border and 0 inside
some_array = np.zeros((3,3))
some_array[:,:][:, [0, 2]] = 1
print(some_array)

#h. Create a 8x8 matrix and fill it with a checkerboard pattern
matrix = np.zeros((8,8))
islice = slice(0, 7, 2)
ifancy = np.arange(0, 7, 2)
matrix[:, islice][ifancy, :] = 1
islice = slice(1, 8, 2)
ifancy = np.arange(1, 8, 2)
matrix[:, islice][ifancy, :] = 1
print(matrix)

#i. Create a checkerboard 8x8 matrix using the tile function
array = np.array([[0, 1], [1, 0]])
board = np.tile(array, (4, 4))
print(board)

#j. Given a 1D array, negate all elements which are between 3 and 8, in place
oned_array = np.arange(11)
oned_array[(oned_array >=3) & (oned_array <= 8)] *= -1
print(oned_array)

#k. Create a random vector of size 10 and sort it
Z = np.random.random(10)
Z = np.sort(Z)
print(Z)

#l. Consider two random array A anb B, check if they are equal
A = np.random.randint(0,2,5)
B = np.random.randint(0,2,5)
equal = np.equal(A,B)
print(equal)

#m. How to convert an integer (32 bits) array into a float (32 bits) in place?
Z = np.arange(10, dtype=np.int32)
print(Z.dtype)
Z = np.float32(Z)
print(Z.dtype)

#n. How to get the diagonal of a dot product?
A = np.arange(9).reshape(3,3)
B = A + 1
C = np.dot(A,B)
D = np.diagonal(C)
print(D)
