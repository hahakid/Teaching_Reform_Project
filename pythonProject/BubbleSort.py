from big_o import big_o
from random import shuffle
from memory_profiler import profile
import pytest


@profile
def bubble_sort(arr):
    n = len(arr)  # 获取数组长度
    for i in range(n):  # 外层循环控制轮次
        for j in range(0, n - i - 1):  # 内层循环比较相邻元素
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # 交换
    return arr  # 返回排序后的数组


def bubble_sort_optimized(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # 标记本轮是否发生交换
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:  # 无交换则提前退出
            break
    return arr
# 测试
#arr = [64, 34, 25, 12, 22, 11, 90]
#print(bubble_sort(arr))  # 输出: [11, 12, 22, 25, 34, 64, 90]
'''
best_case = lambda n: sorted(range(n))  # 最优情况，数组已经有序
worst_case = lambda n: sorted(range(n), reverse=True)  # 最坏情况，数组倒序

# 分析时间复杂度
print("最优情况（已排序数组）：")
best, _ = big_o(bubble_sort, best_case, n_measures=10, min_n=10, max_n=100)
print(best)  # 期望输出：O(n)（优化后）或 O(n^2)（未优化）

print("\n最坏情况（逆序数组）：")
worst, _ = big_o(bubble_sort, worst_case, n_measures=10, min_n=10, max_n=100)
print(worst)  # 期望输出：O(n^2)
'''

'''
# 分析内存占用
for n in [100, 500, 1000]:
    arr = list(range(n, 0, -1))
    bubble_sort(arr.copy())
'''

@pytest.mark.parametrize("sort_func", [bubble_sort, bubble_sort_optimized])
def test_bubble_sort(benchmark, sort_func):
    arr = list(range(200))  # 小规模数据
    shuffle(arr)  # 随机打乱
    result = benchmark(sort_func, arr.copy())
    assert result == sorted(arr.copy())
