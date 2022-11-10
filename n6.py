import numpy as np

def permutation(mat, idx1, idx2): #idx1, idx2 строки, которые будут переставлены
    mat_copy = np.copy(mat)
    mat_copy[[idx1, idx2]] = mat_copy[[idx2, idx1]]
    return mat_copy

M = 5 #строки
N = 10 #столбцы

matrix = np.random.randint(100, size=(M, N))
print("Матрица", matrix, sep="\n")

print("Результат замены", permutation(matrix, 1, 3), "\n", permutation(matrix, 0, 2), sep="\n")

