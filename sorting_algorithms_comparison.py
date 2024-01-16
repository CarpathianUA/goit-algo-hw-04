import random
from timeit import timeit

lst_1000 = [random.randint(0, 1000) for _ in range(1000)]
lst_10000 = [random.randint(0, 10000) for _ in range(10000)]
lst_100000 = [random.randint(0, 100000) for _ in range(100000)]


def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1


def insertion_sort(lst):
    for i in range(1, len(lst)):
        lst = lst[:]
        key = lst[i]
        j = i - 1
        while j >= 0 and key < lst[j]:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst


def print_timing(algorithm_name, sample_size, execution_time):
    print(f"{algorithm_name} ({sample_size} samples): {execution_time:.6f} seconds")


print_timing(
    "Merge Sort", 1000, timeit("merge_sort(lst_1000[:])", globals=globals(), number=1)
)
print_timing(
    "Insertion Sort",
    1000,
    timeit("insertion_sort(lst_1000[:])", globals=globals(), number=1),
)

print_timing(
    "Merge Sort", 10000, timeit("merge_sort(lst_10000[:])", globals=globals(), number=1)
)
print_timing(
    "Insertion Sort",
    10000,
    timeit("insertion_sort(lst_10000[:])", globals=globals(), number=1),
)

print_timing(
    "Merge Sort",
    100000,
    timeit("merge_sort(lst_100000[:])", globals=globals(), number=1),
)
print_timing(
    "Insertion Sort",
    100000,
    timeit("insertion_sort(lst_100000[:])", globals=globals(), number=1),
)

print_timing("TimSort", 1000, timeit("sorted(lst_1000)", globals=globals(), number=1))
print_timing("TimSort", 10000, timeit("sorted(lst_10000)", globals=globals(), number=1))
print_timing(
    "TimSort", 100000, timeit("sorted(lst_100000)", globals=globals(), number=1)
)
