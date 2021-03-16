# Program to multiply two matrices using nested loops
import random

@profile
def genInput(N):
# NxN matrix
    X = []
    Y = []
    result = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
        Y.append([random.randint(0,100) for r in range(N+1)])
        result.append([0] * (N+1))
    return X, Y, result

@profile
def multMatrix(X, Y, result):
# iterate through rows of X
    for i in range(len(X)):
    # iterate through columns of Y
        for j in range(len(Y[0])):
        # iterate through rows of Y
            for k in range(len(Y)):
                result[i][j] += X[i][k] * Y[k][j]
    return result

@profile
def printRes(result):
    for r in result:
        print(r)

N = 250

X, Y, result_zeros = genInput(N)
mult = multMatrix(X, Y, result_zeros)
printRes(mult)
