from matplotlib import pyplot as plt

fig = plt.figure()

ax = fig.add_subplot(111)
box = [0.5, 0.4, 0.3, 0.2]
ax2 = fig.add_axes(box)

ax.plot([0, 100], [0, 200])
ax2.plot([0, 100], [0, 200])

ax.set_xlabel("x")
ax.set_ylabel("y")
ax2.set_xlabel("x")
ax2.set_ylabel("y")

plt.show()