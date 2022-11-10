import numpy as np

def unequal(mat):
    result = np.array([], int)
    count = 0
    for i in mat:
        if np.unique(i).size == 2:
            count += 1
            result = np.append(result, i)
    if result.size > 1:
        result = result.reshape((count, 3))
    return result

matrix = np.random.randint(10, size=(10, 3))
print("Матрица", matrix, sep="\n")

print("Результат", unequal(matrix), sep="\n")