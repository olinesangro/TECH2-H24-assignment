
#TECH2 mandatory assignment - Part A


from math import sqrt

# PArt 1: Using for loops
def std_loops(x):
    """
    Compute standard deviation of x using loops.

    Parameters
    ----------
    x : sequence of numbers
        DESCRIPTION.

    Returns
    -------
    sd : float
        Standard deviation of the list of numbers.

    """
 
    N = len(x)
    mean = sum(x) / N
    sum_sq_diff = sum((xi - mean) ** 2 for xi in x)
    var = sum_sq_diff / N
    return sqrt(var)


#Part 2: Using built-in Functions
def std_builtin(x):
    """
    Conpute standard deviation of x using the built in functions sum() and len().

    Parameters
    ----------
    x : sequence of numbers
        
    Returns
    -------
    float
        Standard deviation of the lsit of numbers

    """
    N = len(x)
    mean = sum(x) / N
    sum_sq = sum(xi ** 2 for xi in x)
    var = (sum_sq /N ) - (mean ** 2)
    return sqrt(var)


# Part 3: using NumPy

import numpy as np

def std_numpy(x):
    return np.std(x)


#Demonstration of the three different ways

num_lst = [1,2,3,4,5]

#using loops
std_loops_res = std_loops(num_lst)
print(f'Standard Deviation using loops: {std_loops_res}')

#Using built-in functions
std_builtin_res = std_builtin(num_lst)
print(f'Standard Deviation using built-in functions: {std_builtin_res}')

#Using NumPy
std_numpy_res = std_numpy(num_lst)
print(f'Standard Deviation using NumPy: {std_numpy_res}')