import matplotlib.pyplot as plt

plt.plot([1, 4, 5, 6, 7], [2, 6, 3, 6, 3], color="red", linewidth=3, linestyle=':', marker='o', mfc='b', markersize=10)
plt.title("Display marker")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.xlim(1, 8)
plt.ylim(1, 8)
plt.show()
