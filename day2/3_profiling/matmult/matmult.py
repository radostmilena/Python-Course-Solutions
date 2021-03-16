# Program to multiply two matrices using nested loops
import random

@profile
def getX(N):
# NxN matrix
    X = []
    for i in range(N):
        X.append([random.randint(0,100) for r in range(N)])
    return X

@profile
def getY(N):
# Nx(N+1) matrix
    Y = []
    for i in range(N):
        Y.append([random.randint(0,100) for r in range(N+1)])
    return Y

@profile
def generateMatrix(N):
# result is Nx(N+1)
    result = []
    for i in range(N):
        result.append([0] * (N+1))
    return result

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

X = getX(N)
Y = getY(N)
result_zeros = generateMatrix(N)
mult = multMatrix(X, Y, result_zeros)
printRes(mult)
