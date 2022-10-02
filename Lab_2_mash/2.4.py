import numpy as np

a = []
n = int(input('Введите коллицество эллементов первого массива: '))
for i in range(n):
    a.append(int(input('Введит эллемент массива с номером ' + str(i + 1) + ': ')))
a1 = np.array(a)
rep = int(input('Введите колличесто повторений: '))
arr = np.tile(a1, rep)
print("Массив: ")
print(arr)