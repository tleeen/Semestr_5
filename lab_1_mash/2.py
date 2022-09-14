import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import AutoMinorLocator, MultipleLocator, FormatStrFormatter

fig, ax = plt.subplots()

N = 50
x = np.random.rand(N)
y = np.random.rand(N)
colors = np.random.rand(N)
area = (30 * np.random.rand(N)) ** 2
plt.scatter(x, y)

x = np.linspace(0, 10, 10000)
ax.plot(x, np.cos(x), color="blue", linewidth=3, label="Синяя линия")
ax.plot(x, np.log(x), color='red', linewidth=5, label="Красная линия")

ax.set_title("Элементы изображения")
ax.set_xlabel("Подпись оси OX")
ax.set_ylabel("Подпись оси OY")

ax.legend()

ax.xaxis.set_minor_locator(AutoMinorLocator())
ax.yaxis.set_minor_locator(AutoMinorLocator())
ax.xaxis.set_major_locator(MultipleLocator())
ax.yaxis.set_major_locator(MultipleLocator())
ax.xaxis.set_minor_formatter(FormatStrFormatter("%.2f"))
ax.tick_params(which='minor', length=5)
ax.tick_params(which='major', length=10)

ax.set_xlim(0, 4)
ax.set_ylim(0, 4)

ax.minorticks_on()
ax.grid(which='minor', color='b', linestyle=':')

ax.spines.right.set_visible(False)
ax.spines.top.set_visible(False)

plt.show()
