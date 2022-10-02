import numpy as np

a = []
b = []
n = int(input('Введите коллицество эллементов первого массива: '))
for i in range(n):
    a.append(int(input('Введит эллемент массива с номером ' + str(i + 1) + ': ')))
n1 = int(input('Введите коллицество эллементов второго массива: '))
for i in range(n1):
    b.append(int(input('Введит эллемент массива с номером ' + str(i + 1) + ': ')))
a1 = np.array(a)
a2 = np.array(b)
arr = np.intersect1d(a1, a2)
print("Массив: ")
print(arr)
