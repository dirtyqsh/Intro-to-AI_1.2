import numpy as np

def four_by_four(mat):
    k = 1
    for i in range(0, 16, 4):
        for j in range(0, 16, 4):
            print(f"Блок {k}", mat[i:i + 4, j:j + 4], sep="\n")
            k += 1
            print("Сумма", np.sum(mat[i:i + 4, j:j + 4]), sep="\n")


matrix = np.random.randint(100, size=(16, 16))
print("Матрица", matrix, sep="\n")

four_by_four(matrix)