import matplotlib.pyplot as plt

fig, ax = plt.subplots()

x = []
y = []
for i in range(-100, 100):
    x.append(i / 10)
for i in x:
    y.append(i * i - i - 6)
ax.plot(x, y)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-5, 5)
ax.set_ylim(-10, 10)
plt.show()
