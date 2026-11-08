"""
Module QuickSort chuyên dụng cho bài toán Tuyển sinh Đại học FPT.
Thực hiện sắp xếp nhanh đa tiêu chí (Multi-criteria QuickSort):
- Tiêu chí 1: Điểm số giảm dần.
- Tiêu chí 2: Mã thí sinh tăng dần theo thứ tự từ điển (ASCII).
Sử dụng phân vùng 3 đoạn Dutch National Flag và khử đệ quy đuôi.
"""
import random
import sys

# Thiết lập giới hạn đệ quy tối đa cho các test case mảng lớn (N <= 100,000)
sys.setrecursionlimit(250000)

def compare_candidates(a, b):
    """
    So sánh thứ tự ưu tiên của hai thí sinh a và b:
    - a: (candidate_id: str, score: float)
    - b: (candidate_id: str, score: float)
    Trả về:
        -1: a có thứ tự ưu tiên cao hơn b (a đứng trước b)
         1: b có thứ tự ưu tiên cao hơn a (b đứng trước a)
         0: a và b tương đương về cả điểm và mã
    """
    # So sánh điểm số: điểm cao hơn đứng trước (giảm dần)
    if a[1] > b[1]:
        return -1
    elif a[1] < b[1]:
        return 1
    
    # Nếu điểm bằng nhau: mã nhỏ hơn đứng trước (tăng dần theo từ điển)
    if a[0] < b[0]:
        return -1
    elif a[0] > b[0]:
        return 1
    return 0

def partition(arr, low, high):
    """
    Phân hoạch 3 phần (Dutch National Flag) với phần tử pivot ngẫu nhiên:
    - Ưu tiên cao hơn pivot: arr[low .. lt-1]
    - Bằng pivot: arr[lt .. gt]
    - Ưu tiên thấp hơn pivot: arr[gt+1 .. high]
    """
    pivot_idx = random.randint(low, high)
    arr[low], arr[pivot_idx] = arr[pivot_idx], arr[low]
    pivot = arr[low]

    lt = low
    gt = high
    i = low + 1

    while i <= gt:
        cmp = compare_candidates(arr[i], pivot)
        if cmp < 0:  # arr[i] có thứ tự ưu tiên cao hơn pivot
            arr[lt], arr[i] = arr[i], arr[lt]
            lt += 1
            i += 1
        elif cmp > 0:  # arr[i] có thứ tự ưu tiên thấp hơn pivot
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1
        else:
            i += 1

    return lt, gt

def quick_sort(arr, low, high):
    """
    Thuật toán QuickSort tối ưu hóa stack bằng kỹ thuật khử đệ quy đuôi:
    Luôn đệ quy vào nhánh nhỏ hơn trước, lặp lại cho nhánh lớn hơn.
    Đảm bảo độ sâu ngăn xếp O(log N).
    """
    while low < high:
        lt, gt = partition(arr, low, high)
        if lt - low < high - gt:
            quick_sort(arr, low, lt - 1)
            low = gt + 1
        else:
            quick_sort(arr, gt + 1, high)
            high = lt - 1

def sort_candidates(candidates):
    """Điểm vào sắp xếp danh sách thí sinh in-place."""
    if len(candidates) > 1:
        quick_sort(candidates, 0, len(candidates) - 1)
    return candidates
