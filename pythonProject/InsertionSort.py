from big_o import big_o
#from random import shuffle
from memory_profiler import profile
#import pytest
import timeit
import random

def insertion_sort(arr):
    for i in range(1, len(arr)):  # 从第2个元素开始
        key = arr[i]  # 当前待插入元素
        j = i - 1
        while j >= 0 and arr[j] > key:  # 向前比较并移动
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # 插入到正确位置
    return arr

def insertion_sort_optimized(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        left, right = 0, i - 1
        # 二分查找插入位置（减少比较次数）
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] < key:
                left = mid + 1
            else:
                right = mid - 1
        # 整体后移
        arr[right+2:i+1] = arr[right+1:i]
        arr[right+1] = key
    return arr


def test_performance():
    sizes = [100, 1000, 5000]  # 不同数据规模
    for size in sizes:
        arr = random.sample(range(size * 10), size)

        # 测试基础版
        time_basic = timeit.timeit(
            lambda: insertion_sort(arr.copy()),
            number=10
        )

        # 测试优化版
        time_optimized = timeit.timeit(
            lambda: insertion_sort_optimized(arr.copy()),
            number=10
        )

        print(f"\n数据规模: {size}")
        print(f"基础版: {time_basic:.5f}s")
        print(f"优化版: {time_optimized:.5f}s")
        print(f"优化幅度: {(1 - time_optimized / time_basic) * 100:.1f}%\n")


if __name__ == "__main__":
    test_performance()
