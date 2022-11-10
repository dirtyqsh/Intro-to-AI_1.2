import numpy as np

def max_meet(ar):
    count = 0
    meet = np.bincount(arr).argmax()
    for i in ar:
        if i == meet:
            count += 1
    return meet, count

arr = np.random.randint(10, size=10)
print("Массив", arr, sep="\n")
print("Элемент, кол-во:", max_meet(arr))