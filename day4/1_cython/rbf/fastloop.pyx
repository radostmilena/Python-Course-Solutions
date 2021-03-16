from math import exp
cimport numpy as np
import numpy as np
from scipy.interpolate import Rbf

def rbf_network_cython(np.ndarray X, np.ndarray beta, int theta):

    cdef int N = X.shape[0]
    cdef int D = X.shape[1]
    cdef float r
    cdef np.ndarray Y = np.zeros(N)
    cdef int i, j, d

    for i in range(N):
        for j in range(N):
            r = 0
            for d in range(D):
                r += (X[j][d] - X[i][d]) ** 2
            r = r**0.5
            Y[i] += beta[j] * exp(-((r * theta)**2))

    return Y
