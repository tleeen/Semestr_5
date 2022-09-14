import matplotlib.pyplot as plt
import math

fig, ax = plt.subplots()

x = []
y = []
for i in range(-1000, 1000):
    x.append(i/10)
for i in x:
    y.append(math.log((i*i+1)*math.exp(-(abs(i)/10)), (1+math.tan(1/(1+math.sin(i)*math.sin(i))))))
ax.plot(x, y)
ax = plt.gca()
ax.spines['left'].set_position('center')
ax.spines['bottom'].set_position('center')
ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)
ax.set_xlim(-40, 40)
ax.set_ylim(-10, 10)
plt.show()