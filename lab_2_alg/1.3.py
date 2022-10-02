import matplotlib.pyplot as plt
import timeit


def selection_sort(nums):
    for i in range(len(nums)):
        lowest_value_index = i
        for j in range(i + 1, len(nums)):
            if nums[j] < nums[lowest_value_index]:
                lowest_value_index = j
        nums[i], nums[lowest_value_index] = nums[lowest_value_index], nums[i]


def partition(nums, low, high):
    pivot = nums[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while nums[i] < pivot:
            i += 1
        j -= 1
        while nums[j] > pivot:
            j -= 1
        if i >= j:
            return j
        nums[i], nums[j] = nums[j], nums[i]


def quick_sort(nums):
    def _quick_sort(items, low, high):
        if low < high:
            split_index = partition(items, low, high)
            _quick_sort(items, low, split_index)
            _quick_sort(items, split_index + 1, high)

    _quick_sort(nums, 0, len(nums) - 1)


a = [i for i in range(100, 1000)]
time = [[], []]
for i in a:
    arr = [_ for _ in range(i, 0, -1)]
    time[0].append(timeit.timeit(f"selection_sort({arr})", number=1, globals=globals()))
    time[1].append(timeit.timeit(f"quick_sort({arr})", number=1, globals=globals()))

plt.plot(a, time[0], label="Сортировка выбором")
plt.plot(a, time[1], label="Быстрая сортировка")
plt.legend()
plt.xlabel("Размер входных данных")
plt.ylabel("Время выполнения алгоритма")
plt.title("Отсортированный в обратную сторону список")
plt.show()
plt.close()
