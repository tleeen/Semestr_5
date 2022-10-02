import numpy as np

n = 3.09066280756759
arr = np.array([0.5, 1.8, 2.1, 3.5, 4.87, 5.13, 6.49])
i = (np.abs(arr - n).argmin())
print("Ближайший эллемент: ")
print(arr[i])