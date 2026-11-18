import random


def bubble_sort(arr):
    a = arr.copy()
    n = len(a)
    iterations = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            iterations += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break

    return a, iterations


def selection_sort(arr):
    a = arr.copy()
    n = len(a)
    iterations = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            iterations += 1
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]

    return a, iterations


def quick_sort(arr, iterations=None):
    if iterations is None:
        iterations = [0]

    if len(arr) <= 1:
        return arr, iterations[0]

    pivot = arr[len(arr) // 2]
    left, middle, right = [], [], []

    for x in arr:
        iterations[0] += 1
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    sorted_left, _ = quick_sort(left, iterations)
    sorted_right, _ = quick_sort(right, iterations)

    return sorted_left + middle + sorted_right, iterations[0]


sizes = [10, 50, 100, 500, 1000]

print(f"{'Розмір (N)':<12} | {'Бульбашка':<15} | {'Вибірка':<15} | {'Швидке (Quick)':<15}")
print("-" * 65)

for size in sizes:
    test_data = [random.randint(1, 10000) for _ in range(size)]

    _, iter_bubble = bubble_sort(test_data)
    _, iter_selection = selection_sort(test_data)
    _, iter_quick = quick_sort(test_data)

    print(f"{size:<12} | {iter_bubble:<15} | {iter_selection:<15} | {iter_quick:<15}")