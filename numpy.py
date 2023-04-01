print("Hey welcome to the world of machine learning!")

import numpy as  np
a=np.array([1,2,3])
print(type(a))
print(a)

print(a[2])

a[2]=10
print(a)

#creating 2-d numpy array

b=np.array([[1,3,5],[2,7,9]])
print(b)
print(b.shape)

import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9],[10,11,12]])
print(a)
print(a.shape)
b=a[1:,2:]
print(b)


a=np.array([[1,2,3],[7,9,6]])
b=np.array([[7,6,9],[6,10,2]])
print(a)
print(b)
#matrix addition
print(a+b)
#matrix substraction
print(a-b)
#matrix multiplication
print(a*b)
#matrix division
print(a/b)
#matrix square root
print(np.sqrt(a))
#sum of each array
print(np.sum(a))
#giving the row sum of an array
print(np.sum(a,axis=0))
#giving the column sum of an array
print(np.sum(a,axis=1))
#transopose of a matrix
print(a.T)
