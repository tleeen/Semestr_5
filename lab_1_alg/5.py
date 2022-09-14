import matplotlib.pyplot as plt
import timeit


def foo1(q):
    a = 100 in q
    return a

def foo2(q):
    a = 100 in q
    return a


x = set()
y = []
z = []
for i in range(100):
    x.add(i)
    y.append(i)
    z.append(i)

time1 = []
time2 = []
for i in range(100):
    time1.append(timeit.timeit(
        f"foo1({x})", number=5, globals=globals()))
    time2.append(timeit.timeit(
        f"foo2({y})", number=5, globals=globals()))
fig = plt.figure()

ax = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax.plot(z, time1)
ax.set_xlabel('Входные данные')
ax.set_ylabel('Время выполнения функции')
ax2.plot(z, time2)
ax2.set_xlabel('Входные данные')
ax2.set_ylabel('Время выполнения функции')
plt.show()