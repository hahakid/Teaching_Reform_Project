from big_o import big_o
from random import shuffle
from memory_profiler import profile
import pytest

@profile
def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i  # 假设当前位置是最小值
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j  # 更新最小值索引
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 交换
    return arr
@profile

def selection_sort_optimized(arr):
    n = len(arr)
    for i in range(n//2):          # 外层循环减半
        min_idx, max_idx = i, i
        for j in range(i, n-i):    # 内层循环双向扫描
            if arr[j] < arr[min_idx]:
                min_idx = j
            if arr[j] > arr[max_idx]:
                max_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        if max_idx == i:           # 处理最大值被移动的情况
            max_idx = min_idx
        arr[n-i-1], arr[max_idx] = arr[max_idx], arr[n-i-1]
    return arr

'''
best_case = lambda n: sorted(range(n))  # 最优情况，数组已经有序
worst_case = lambda n: sorted(range(n), reverse=True)  # 最坏情况，数组倒序

#分析时间复杂度
print("普通版最优情况（已排序数组）：")
best, _ = big_o(selection_sort, best_case, n_measures=10, min_n=1000, max_n=5000)
print(best)  # 期望输出：O(n)（优化后）或 O(n^2)（未优化）

print("\n普通版最坏情况（逆序数组）：")
worst, _ = big_o(selection_sort, worst_case, n_measures=10, min_n=1000, max_n=5000)
print(worst)  # 期望输出：O(n^2)

#分析时间复杂度
print("\n改进版最优情况（已排序数组）：")
best, _ = big_o(selection_sort_optimized, best_case, n_measures=10, min_n=1000, max_n=5000)
print(best)  # 期望输出：O(n)（优化后）或 O(n^2)（未优化）

print("\n改进版最坏情况（逆序数组）：")
worst, _ = big_o(selection_sort_optimized, worst_case, n_measures=10, min_n=1000, max_n=5000)
print(worst)  # 期望输出：O(n^2)
'''

for n in [100, 500, 1000]:
    arr = list(range(n, 0, -1))
    selection_sort(arr.copy())
    selection_sort_optimized(arr.copy())
