import random

def partition(arr, low, high):
    """Phân đoạn 3 phần Dutch National Flag với pivot ngẫu nhiên"""
    pivot_idx = random.randint(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
    pivot = arr[low]
    lt, gt = low, high
    i = low + 1
    while i <= gt:
        if arr[i] < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif arr[i] > pivot:
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1
    return lt, gt

def quick_sort(arr, low, high):
    if low < high:
        lt, gt = partition(arr, low, high)
        quick_sort(arr, low, lt - 1)
        quick_sort(arr, gt + 1, high)

def sort_numbers(arr):
    if len(arr) > 1:
        quick_sort(arr, 0, len(arr) - 1)
    return arr
