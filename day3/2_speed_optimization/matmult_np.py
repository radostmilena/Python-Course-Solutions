# Program to multiply two matrices using numpy
import numpy as np

@profile
def getInput(N):
    X = np.random.rand(N, N)
    Y = np.random.rand(N, N+1)
    return X, Y

@profile
def multMatrix(X, Y):
     result = np.dot(X, Y)
     return result

@profile
def printRes(result):
    for r in result:
        print(r)

N = 250

X, Y = getInput(N)
mult = multMatrix(X, Y)
printRes(mult)
