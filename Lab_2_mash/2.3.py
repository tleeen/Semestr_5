import numpy as np

a = []
n = int(input('Введите коллицество эллементов первого массива: '))
for i in range(n):
    a.append(int(input('Введит эллемент массива с номером ' + str(i + 1) + ': ')))
arr = np.array(a)
un, count = np.unique(arr, return_counts=True)
print("Уникальные эллементы и их частоты: ")
print(un, ',', count)
