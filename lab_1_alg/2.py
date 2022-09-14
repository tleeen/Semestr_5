import random
import matplotlib.pyplot as plt
import string
import timeit


def foo1(s):
    slovo = str(s)
    a = []
    b = []
    l = len(s)
    for i in range(l):
        a.append(slovo[i])
    for i in range(l):
        b.append(slovo[i])
    for i in range(l // 2):
        c = a[i]
        a[i] = a[-1 - i]
        a[-1 - i] = c
    if a == b:
        print("It's palindrome")
    else:
        print("It's not palindrome")


def foo2(s):
    slovo = str(s)
    l = len(s)
    for i in range(l // 2):
        if slovo[i] != slovo[-1 - i]:
            print("It's not palindrome")
            break
    else:
        print("It's palindrome")


def generate_random_str(arr):
    letters_and_digits = string.ascii_letters + string.digits
    rand_str = ''.join([random.choice(letters_and_digits)
                        for _ in range(arr)])
    return rand_str


foo1('12321')
foo2('12321')
arr = [10, 25, 50, 100, 250, 500, 1000, 2500, 5000, 10000]
time1 = []
time2 = []
for i in arr:
    rand_str = generate_random_str(i)
    time1.append(timeit.timeit(
        f"foo1('{rand_str}')", number=5, globals=globals()))
    time2.append(timeit.timeit(
        f"foo2('{rand_str}')", number=5, globals=globals()))
fig = plt.figure()

ax = fig.add_subplot(1, 2, 1)
ax2 = fig.add_subplot(1, 2, 2)

ax.plot(arr, time1)
ax.set_xlabel('Входные данные')
ax.set_ylabel('Время выполнения функции')
ax2.plot(arr, time2)
ax2.set_xlabel('Входные данные')
ax2.set_ylabel('Время выполнения функции')
plt.show()
