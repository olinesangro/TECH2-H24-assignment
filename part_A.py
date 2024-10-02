
# TECH2 mandatory assignment - Part A

from math import sqrt #Import the built-in function in order to compute the square root

num_lst= [1,2,3,4,5]


# FOR LOOPS

def std_loops(x):
    """
    
    Parameters
    ----------
    x : sequence of numbers

    Returns
    -------
    Float
        Standard deviation of the list of numbers

    """
    N = len(num_lst)
    
    # Calculate the mean:
    total = 0                   # Initialize total to o
    for num in num_lst:
        total += num            # Add each number to total
    mean = total / N
    
    # Calculate the variance
    var_sum = 0                         #Initialize var_sum to 0
    for num in num_lst:
        var_sum += (num - mean) ** 2    #Add squared difference to var_sum
        var = var_sum / N
        
        
    # Calculate the standard deviation
    return sqrt(var)

print('Standard deviation using loops: ', std_loops(num_lst))



# BUILT_IN FUNCTIONS: SUM and LEN

def std_builtin(x):
    """
    
    Parameters
    ----------
    x : sequence of numbers

    Returns
    -------
    float
        Standard deviation of the list of numbers

    """

    # Define N 
    N = len(x)   
    
    # Calculate the mean
    mean = sum(x)/N

    # Calculate the mean of squares
    mean_of_squares = sum(num**2 for num in x)/N

    # Calculate the variance
    var = mean_of_squares - mean ** 2

    # Calculate the standard deviation
    return sqrt(var)

print('Standard deviation using built in fuctions:' , std_builtin(num_lst))
    



# NUMPY
import numpy as np

def std_numpy(x):
    """
    
    Parameters
    ----------
    x : sequence of numbers

    Returns
    -------
    float
        Standars deviation of the list of numbers

    """
    return np.std(x)

print('Standard deviation using NumPY:', std_numpy(num_lst))

    