import numpy as np

def three_to_eight(arr):
    arr[(arr > 3) & (arr < 8)] *= -1
    return arr

arr1 = np.random.randint(10, size=10)
arr2 = np.random.randint(10, size=10)
arr3 = np.random.randint(10, size=10)

print("Массивы:", arr1, arr2, arr3, sep="\n")

print("Результат: ", three_to_eight(arr1), three_to_eight(arr2), three_to_eight(arr3), sep="\n")