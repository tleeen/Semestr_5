import numpy as np

arr = np.zeros((4, 4))
arr[::2, 1::2] = 1
arr[1::2, ::2] = 1
print("Массив: ")
print(arr)