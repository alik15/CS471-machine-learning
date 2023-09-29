import numpy as np

from scipy.optimize import root
from scipy.optimize import minimize
from scipy.sparse import csr_matrix 
from scipy import interpolate
from scipy.interpolate import interp1d


def function(x):
    return 3*(x**2)  + 2*x - 10

initial_guess = 1.0

result = root(function,initial_guess)
print(result)


 
# task b

def function_2(x):
    return (x**2) - 20*x + 45
# task c 
csr_matrix(5,4)




#task d-- interpolation
list1=list(range(1,11))
print(list1)

def func_1(x):
   return  2*x + 1 

list2 = [func_1(x) for x in list1]
print(list2)

interp_func = interp1d(list1,list2)


print(interp_func(3.5))
print(interp_func(5))
print(interp_func(99))