import numpy as np

array = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
#print(array[:2,0:2]) #Prints [4 5],[7,8]
#Try to reduce to ecehlon
array[2] = 4*array[2]
array[2] = -7*array[1] + array[2]
array[1] = -4*array[0] + array[1]
array[2] = -1*array[1] + array[2]
array[1] = -1/3*array[1]
array[0] = -2*array[1] + array[0]
print(array)