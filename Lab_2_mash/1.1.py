import numpy as np

arr = np.array([1, 7, 13, 105])
print("Массив занимает: ", "%d bytes" % (arr.size * arr.itemsize))
np.savetxt('arr.txt', arr)
arr_t = np.loadtxt('arr.txt', dtype=int)
print("Массив из текстового файла: ", arr_t)
np.save('arr', arr)
arr_b = np.load('arr.npy')
print("Массив из бинарного файла: ", arr_b)
