import numpy as np
#creating array using numpy
# arr = np.array([1,2,38,4,5,5.1])
# print(arr)
# #print the type numpy array
# print(type(arr))
# print(arr.max())
# print(arr.min())
# print(arr.mean())
# print(arr.sum())

def reverseSorting(arr):
    arr.sort(reverse = True)
    return arr

array = [1,2,3,4,5]
sorted_array = reverseSorting(array)
print(sorted_array)



