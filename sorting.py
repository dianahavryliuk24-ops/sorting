import random

def bubble_sort(arr):
    arr = arr.copy()
    iterations = 0

    for i in range(len(arr)):
        for j in range(0, len(arr) - i - 1):
            iterations += 1
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr, iterations

def selection_sort(arr):
    arr = arr.copy()
    iterations = 0

    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            iterations += 1
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr, iterations

def quick_sort(arr):
    iterations = 0

    def sort(sub_arr):
        nonlocal iterations
        if len(sub_arr) <= 1:
            return sub_arr

        pivot = sub_arr[len(sub_arr) // 2]
        left = []
        middle = []
        right = []

        for x in sub_arr:
            iterations += 1
            if x < pivot:
                left.append(x)
            elif x == pivot:
                middle.append(x)
            else:
                right.append(x)

        return sort(left) + middle + sort(right)

    result = sort(arr)
    return result, iterations

test_array = [38, 27, 43, 3, 9, 82, 10]

print("Початковий масив:", test_array)
print("Бульбашка:", bubble_sort(test_array))
print("Вибірка:  ", selection_sort(test_array))
print("Швидке:   ", quick_sort(test_array))
print()

sizes = [10, 50, 100, 500, 1000]

print(f"{'Розмір (N)':<12} | {'Бульбашка':<15} | {'Вибірка':<15} | {'Швидке':<15}")
print("-" * 65)

for size in sizes:
    array = [random.randint(1, 10000) for _ in range(size)]

    _, bubble_iter = bubble_sort(array)
    _, selection_iter = selection_sort(array)
    _, quick_iter = quick_sort(array)

    print(f"{size:<12} | {bubble_iter:<15} | {selection_iter:<15} | {quick_iter:<15}")
