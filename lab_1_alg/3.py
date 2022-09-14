import matplotlib.pyplot as plt

x = []
y1 = []
y2 = []
for i in range(-20, 20):
    x.append(i)
for i in x:
    y1.append(i * i - i - 10)
for i in x:
    y2.append(4 * i + 40)

plt.plot(x, y1, label="T1")
plt.plot(x, y2, label="T2")
plt.grid(True)
plt.xlim(-11, 11)
plt.legend()
plt.show()
