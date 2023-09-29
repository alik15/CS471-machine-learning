import numpy as np 


array1 = np.array([[10,2,3,4,5],
                  [1,2,3,4,5],
                  [1,2,3,4,5],
                  [1,2,3,4,5],
                  [1,2,3,4,5]]
                 )

array2 = np.array([
    [1,1,1,1,1],
    [2,2,2,2,2],
    [3,3,3,3,3],
    [4,4,4,4,4],
    [5,5,5,5,5]
])
print("print the arrays: ")
print(array1,array2)
print("sum of two matrices: ")
print(array1+array2)


print("difference of two matrices: ")
print(array1-array2)

print("elementwise product of the two matrices: ")
print(array1*array2)

print("elementwise division of the matrix: ")
print(array1/array2)


print("matrix multiplication")
print(np.matmul(array1,array2))



