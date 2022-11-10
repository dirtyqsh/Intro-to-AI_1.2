import numpy as np

def average(ar, mat):
    ar = np.mean(ar)
    mat = mat - ar
    return mat

# Не писал несколько примеров, так как массив + матрица рандомные
arr = np.random.randint(10, size=10)
print("Массив", arr, sep="\n")

matrix = np.random.randint(100, size=(5, 5))
print("Матрица", matrix, sep="\n")

print("Результат", average(arr, matrix), sep="\n")