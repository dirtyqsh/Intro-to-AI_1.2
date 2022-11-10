import numpy as np

matrix = np.random.randint(100, size=(5, 5))
print("Матрица", matrix, sep="\n")

average_matrix = np.mean(matrix[:, :], axis=1)
average_matrix = average_matrix.reshape((5, 1))
print("Средние значения", average_matrix, sep="\n")


result_matrix = matrix - average_matrix
print("Результат", result_matrix, sep="\n")
