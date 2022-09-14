from matplotlib import pyplot as plt

fig = plt.figure(figsize=(15, 3))

ax = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax.plot([0, 100], [0, 200], color="blue", linewidth=6)

x = []
y = []
for i in range(1, 1000):
    x.append(i/10)
for i in x:
    y.append(i*i)

ax2.plot(x, y, color="red", linewidth=3, linestyle='--')

plt.show()