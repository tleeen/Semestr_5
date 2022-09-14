import matplotlib.pyplot as plt
import numpy as np
from scipy.interpolate import interp1d


z = [2, 2, 2, 2, 2, 3, 4, 4, 4, 4, 5, 5, 5, 5, 5, 6, 6, ]
x = [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 6, 7, 8]
y = [0, 0.10, 0.15, 0.17, 0.12, 0.08, 0.10, 0.22, 0.26, 0.22, 0.04, 0]

x_new = np.linspace(min(x), max(x), 500)

f1 = interp1d(x, y, kind='cubic')
y_smooth = f1(x_new)

fig = plt.figure()
cc = plt.hist(z, [0, 1, 2, 3, 4, 5, 6, 7, 8], density=True, color='red', alpha=0.2)
ax = plt.plot(x_new, y_smooth, color='red')
plt.xlabel("petal_length")
plt.show()
