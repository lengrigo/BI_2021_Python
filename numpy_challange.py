import numpy as np

# # Test arrays
# matrix1 = np.array([[1, 2, 3], [4, 5, 6], [3, 2, 9]])
# matrix2 = np.array([[3, 6, 4], [9, 5, 3], [1, 4, 4]])
# matrix3 = np.array([[2, 5], [5, 0], [2, 5]])
# lst = [matrix1, matrix2, matrix3]
# arr1 = np.array([7, 2])
# arr2 = np.array([5, 8])
# arr5 = np.array([[5, 5],
#                  [2, 3],
#                  [4, 5],
#                  [1, 1]])


# 1: three ways to make numpy array (function returns the list with 3 arrays)
def new_arrays():
    x = np.array([5, 10, 15])
    y = np.arange(8)
    z = np.zeros((4, 7))
    return [x, y, z]


# # Test call for 1
# print("First: ", new_arrays())


# 2: function that takes two matrices, multiplies them and returns the result
def matrix_multiplication(matrix1, matrix2):
    result = np.array(matrix1) * np.array(matrix2)
    return result


# # Test call for 2
# second = matrix_multiplication(matrix1, matrix2)
# print("Second:", second)


# 3: function that takes list of matrices and
# returns True if they can be multiplied and False if not
def multiplication_check(lst):
    try:
        for i in range(1, len(lst) - 1):
            lst[i] * lst[i + 1]
    except ValueError:
        return False
    else:
        return True


# # Test call for 3
# third = multiplication_check(lst)
# print('Third:', third)


# 4: function, that takes the list of matrices and
# returns the result of multiplying if they can be multiplied and None if not
def multiply_matrices(lst):
    result = lst[0]
    try:
        for i in range(1, len(lst)):
            result = result * lst[i]
    except ValueError:
        return None
    else:
        return result


# # Test call for 4
# fourth = multiply_matrices(lst)
# print("Fourth:", fourth)


# 5: function that count distance between two dots
def compute_2d_distance(arr1, arr2):
    result = np.sqrt((arr1 - arr2) ** 2 + (arr1[1] - arr2[1]) ** 2)
    return result


# # Test call for 5
# fifth = compute_2d_distance(arr1, arr2)
# print('Fifth', fifth)


# 6: function that count distance between two arrays with the same length
def compute_multidimensional_distance(arr3, arr4):
    result = np.sqrt(((arr3 - arr4) ** 2).sum())
    return result


# # Test call for 6
# sixth = compute_multidimensional_distance(arr1, arr2)
# print('Sixth: ', sixth)


# 7: function for pairwise distance matrix
def compute_pair_distances(arr5):
    result = np.zeros((arr5.shape[0], arr5.shape[0]))
    for i in range(arr5.shape[0]):
        for j in range(i, arr5.shape[0]):
            result[i][j] = result[j][i] = np.sqrt(((arr5[i] - arr5[j]) ** 2).sum())
    return result


# # Test call for 7
# seventh = compute_pair_distances(arr5)
# print('Seventh: ', seventh)
