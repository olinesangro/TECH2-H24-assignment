
#TECH2 mandatory assignment - Part A


from math import sqrt #Import the built-in function in order to compute the square root

num_lst= [1,2,3,4,5]
N = len(num_lst)

def std_dev(x):
    
    #Calculate the mean:
    total = 0
    for num in num_lst:
        total += num
    mean = total / N
    
    #Calculate the variance
    var_sum = 0
    for num in num_lst:
        var_sum += (num - mean) ** 2
        var = var_sum / N
        
        
    #Calculate the standard deviation
    return sqrt(var)

print(std_dev(num_lst))
