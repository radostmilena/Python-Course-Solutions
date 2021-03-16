import simple_math as sm
import numpy as np

def test_simple_math():
    assert sm.simple_add(1, 2) + sm.simple_sub(1,2) == 2
    assert sm.simple_mult(1, 2) * sm.simple_div(1, 2) == 1
    assert (sm.poly_first(np.zeros(3), 5, 2.5) == 5).all() == True
    assert (sm.poly_second(np.zeros(3), 5, 2.5, 1.5) == 5).all() == True
