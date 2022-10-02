import numpy as np

c = []
b = []

print(f"Введите коэффициенты и свободный член первого уравнения:")
data = input().split()
while len(data) != 3:
    print("Введите данные повторно")
    data = input().split()
c.append(list(map(int, data[:-1])))
b.append(int(data[-1]))

print(f"Введите коэффициенты и свободный член второго уравнения:")
data = input().split()
while len(data) != 3:
    print("Введите данные повторно")
    data = input().split()
c.append(list(map(int, data[:-1])))
b.append(int(data[-1]))

if np.linalg.det(c) != 0:
    x = np.linalg.solve(c, b)
    print(x)
else:
    print("Система не имеет решений (или имеет их бесконечно много)")
