from numpy.distutils.core import setup
from Cython.Build import cythonize
import numpy

setup(
    ext_modules = cythonize("fastloop.pyx")
)
