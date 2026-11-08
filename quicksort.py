import random
import sys

# Tăng giới hạn đệ quy để chịu tải các test case mảng lớn
sys.setrecursionlimit(200000)

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
    """Khử đệ quy đuôi để tối ưu độ sâu ngăn xếp O(log N)"""
    while low < high:
        lt, gt = partition(arr, low, high)
        # Đệ quy trên phân vùng nhỏ hơn trước, lặp cho phân vùng lớn hơn
        if lt - low < high - gt:
            quick_sort(arr, low, lt - 1)
            low = gt + 1
        else:
            quick_sort(arr, gt + 1, high)
            high = lt - 1

def sort_numbers(arr):
    if len(arr) > 1:
        quick_sort(arr, 0, len(arr) - 1)
    return arr
