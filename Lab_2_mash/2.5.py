import numpy as np

a = np.array([200, 300, np.nan, np. nan, np.nan, 700])
arr = a[np.isfinite(a)]
print("Массив: ")
print(arr)