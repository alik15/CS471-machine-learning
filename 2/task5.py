import numpy as np 



array = np.array([[10,2,3,4,5],
                  [1,2,3,4,5],
                  [1,2,3,4,5],
                  [1,2,3,4,5],
                  [1,2,3,4,5]]
                 )
print(array[4,4])
print("printing rows 2 and 3 via slicing: ")
print(array[2])
print(array[3])

print("sum of matrix in numpy: ")
print(array.sum())

print("sum of the matrix elements along axis 0: ")
print(array[0].sum())
print(array[1].sum())

print("compute mean of the matrix elements: ")
print(array.mean())

print("standard deviation of matrix elements: ")
print(array.std())

