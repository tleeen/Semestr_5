import numpy as np

a = []
n = int(input('Введите коллицество эллементов первого массива: '))
for i in range(n):
    a.append(int(input('Введит эллемент массива с номером ' + str(i + 1) + ': ')))
a1 = np.array(a)
arr = np.unique(a1)
print("Массив: ")
print(arr)