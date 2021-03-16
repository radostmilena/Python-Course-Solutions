"""
A collection of simple math operations
"""

def simple_add(a,b):
    """
    Add two numbers a and b. 

    Parameters
    ----------
    a 
        First addend
    b
        Second addend

    Returns
    -------
    a+b
        Sum of both numbers

    Examples
    --------
    >>> simple_add(2, 1)
    3
    """
    return a+b

def simple_sub(a,b):
    """
    Subtract two numbers a and b. 

    Parameters
    ----------
    a 
        Minuend
    b
        Subtrahend

    Returns
    -------
    a-b
        Difference of both numbers

    Examples
    --------
    >>> simple_sub(2, 1)
    1
    """
    return a-b

def simple_mult(a,b):
    """
    Multiply two numbers a and b. 

    Parameters
    ----------
    a 
        First factor
    b
        Second factor

    Returns
    -------
    a*b
        Product of both numbers

    Examples
    --------
    >>> simple_mult(2, 1)
    2
    """
    return a*b

def simple_div(a,b):
    """
    Divide two numbers a and b. 

    Parameters
    ----------
    a 
        Dividend 
    b
        Divisor   

    Returns
    -------
    a/b
        Quotient of both numbers

    Examples
    --------
    >>> simple_div(2, 1)
    2
    """
    return a/b

def poly_first(x, a0, a1):
    """
    Generate first oder polynomial (linear equation).

    Parameters
    ----------
    a0
        y-intercept
    a1
        slope 
    x : array-like
        Input array of x values.     

    Returns
    -------
    a0 + a1*x : array-like 
        y values of the linear equation.

    Examples
    --------
    >>> poly_first(np.random.rand(5), 2, 1)
    array([2.38828177, 2.72971298, 2.81972427, 2.2786672 , 2.42738528])
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """
    Generate second oder polynomial (quadratic equation).

    Parameters
    ----------
    a0, a1, a2
        Coefficients
    x : array-like
        Input array of x values.     

    Returns
    -------
    poly_first(x, a0, a1) + a2*(x**2) : array-like 
        y values of the linear equation (poly_first) plus quadratic term (x**2).

    Examples
    --------
    >>> poly_second(np.random.rand(5), 2, 1, 1)
    array([2.29194688, 2.6436297 , 2.26655097, 3.03225692, 2.94207625])
    """
    return poly_first(x, a0, a1) + a2*(x**2)
