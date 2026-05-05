import numpy as np


# NumPy is used to work with arrays. The array object in NumPy is called ndarray.

# We can create a NumPy ndarray object by using the array() function.

arr = np.array([1, 2, 3, 4, 5])
print(arr)

# NumPy arrays are faster than Python lists because they are stored in contiguous memory locations and have a fixed data type.
# NumPy arrays can be multi-dimensional. We can create a 2D array by passing a list of lists to the array() function.
arr2d = np.array([[1, 2, 3], [4, 5, 6]])

print(arr2d)

#print 3d array
arr3d = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
print(arr3d)


#NumPy Array Indexing
# NumPy arrays can be indexed and sliced in a similar way to Python lists, but they also support more advanced indexing techniques.
# We can access individual elements in a NumPy array using square brackets and the index of the element.
print(arr[0])  # Output: 1
print(arr2d[0][1])  # Output: 2
print(arr3d[0][1][0])  # Output: 3

