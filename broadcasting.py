# Broadcasting in numpy allows for you to add/subtract matrices of different size
# where in regular math you cant. they need to contain the same amomunt of colunms.
import numpy as np

A = np.array([
    [1,1,1],
    [1,1,1],
    [1,1,1]
    ])
#print(A.shape)
B = np.array([2,2,2])
#print(B.shape)
C = np.array([
    [10],[20],[30]
])
#print(C.shape)
D = np.array([10])
#print(D.shape)
# print(A+B)
# print(A+C)
# print(A+D)
# BD = (B+D)
# print(BD.shape)

array1 = np.array([
    [1,2,3,4,5],
    [1,2,3,4,5]])
print(np.sum(array1))
print(np.sum(array1[1,:]))
print(np.sum(array1,axis=0))
print(np.sum(array1,axis=1))