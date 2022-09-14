import matplotlib.pyplot as plt
import timeit


def foo(n):  # n - число
    res = []
    for i in range(1, n + 1):
        divisors = 0
        j = 2
        while j < i and divisors == 0:
            if i % j == 0:
                divisors += 1
            j += 1
        print(divisors)
        if divisors == 0:
            res.append(i)
    return res


arr = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
time = []
for i in arr:
    time.append(timeit.timeit(f"foo({i})", number=5, globals=globals()))

plt.plot(arr, time)
plt.xlabel('Входные данные')
plt.ylabel('Время выполнения функции')
plt.show()
