import numpy as np

def max_n(mat):
    n = int(input("Введите n: "))
    arr = np.array(mat).ravel()
    arr_sort = np.argsort(arr)
    arr_sort = arr[arr_sort]
    result = arr_sort[-n:]
    print(f"{n} наибольших элемента:", result)


matrix = np.random.randint(100, size=(5, 5))
print("Матрица", matrix, sep="\n")

max_n(matrix)

