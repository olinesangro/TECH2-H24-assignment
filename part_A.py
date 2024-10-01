
#TECH2 mandatory assignment - Part A


from math import sqrt #Import the built-in function in order to compute the square root

num_lst= [1,2,3,4,5]

def std_dev(num_lst):
    for num in num_lst:
        N = 1/len(num_lst)
        S = 1/N*(num * num**2)
        var = sqrt(S - num**-2)
    return std_dev(sqrt(var))
