import matplotlib.pyplot as plt

plt.plot([2, 3, 5, 6, 8], [1, 5, 10, 18, 20], linewidth=0, marker='*', markerfacecolor='b')
plt.plot([3, 4, 6, 7, 9], [2, 6, 11, 20, 22], linewidth=0, marker='o', markerfacecolor='r')
plt.xlim(0, 10)
plt.ylim(0, 30)
plt.show()
