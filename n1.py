import numpy as np

matrix = np.ones((10, 10))

matrix[1:-1, 1:-1] = 0

print(matrix)