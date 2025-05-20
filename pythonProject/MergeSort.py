import random
from memory_profiler import memory_usage
import unittest

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge_sort_BU(arr):
    n = len(arr)
    size = 1
    while size < n:
        for i in range(0, n, size * 2):
            mid = i + size - 1
            right = min(i + size * 2 - 1, n - 1)
            merge(arr, i, mid, right)
        size *= 2


def merge(arr, l, m, r):
    # Trae 修正
    if not arr or l > m or m >= r:
        return

    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2

    for i in range(0, n1):
        L[i] = arr[l + i]

    for j in range(0, n2):
        R[j] = arr[m + 1 + j]

    i = j = 0
    k = l

    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

'''
class TestMergeFunction(unittest.TestCase):

    def test_merge_sorted_arrays(self):
        arr = [1, 3, 5, 7, 2, 4, 6, 8]
        arr1 = [1, 3, 5, 7, 9]
        arr2 = [1, 3, 5, 7, 9]
        merge(arr1, 0, 3, 7)
        self.assertEqual(arr1, [1, 2, 3, 4, 5, 6, 7, 8])

    def test_merge_with_duplicates(self):
        arr = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
        merge(arr, 0, 2, 9)
        self.assertEqual(arr, [1, 2, 2, 3, 3, 3, 4, 4, 4, 4])

    def test_merge_single_element_arrays(self):
        arr = [1, 2]
        merge(arr, 0, 0, 1)
        self.assertEqual(arr, [1, 2])

    def test_merge_empty_array(self):
        arr = []
        merge(arr, 0, 0, 0)
        self.assertEqual(arr, [])

    def test_merge_all_elements_same(self):
        arr = [5, 5, 5, 5, 5]
        merge(arr, 0, 1, 4)
        self.assertEqual(arr, [5, 5, 5, 5, 5])
        
    # 非必要case，因为合并的一定是有序的
    #def test_merge_reverse_sorted_arrays(self):
    #    arr = [5, 4, 3, 2, 1]
    #    merge(arr, 0, 1, 4)
    #    self.assertEqual(arr, [1, 2, 3, 4, 5])

    def test_merge_reverse_sorted_arrays(self):
        # 修改后的测试数据：两个子数组各自有序但整体无序
        # 左子数组 [7,5] 右子数组 [4,3] -> 合并后应为 [4,3,5,7,1]
        arr = [5, 7, 3, 4, 1]
        merge(arr, 0, 1, 3)  # 合并索引0-1([7,5])和2-3([4,3])
        self.assertEqual(arr, [3, 4, 5, 7, 1])

    def test_merge_with_negative_numbers(self):
        arr = [-3, -1, -2, 0]
        merge(arr, 0, 1, 3)
        self.assertEqual(arr, [-3, -2, -1, 0])
'''


class TestMergeSort(unittest.TestCase):
    # 测试空数组
    def test_empty_array(self):
        # 断言merge_sort([])的结果为[]
        self.assertEqual(merge_sort([]), [])

    # 测试只有一个元素的数组
    def test_single_element_array(self):
        # 断言merge_sort([1])的结果为[1]
        self.assertEqual(merge_sort([1]), [1])

    # 测试已经排序的数组
    def test_sorted_array(self):
        # 断言merge_sort([1, 2, 3, 4, 5])的结果为[1, 2, 3, 4, 5]
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    # 测试逆序排序的数组
    def test_reverse_sorted_array(self):
        # 断言merge_sort([5, 4, 3, 2, 1])的结果为[1, 2, 3, 4, 5]
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    # 测试未排序的数组
    def test_unsorted_array(self):
        # 断言merge_sort([3, 1, 4, 1, 5, 9, 2, 6])的结果为[1, 1, 2, 3, 4, 5, 6, 9]
        self.assertEqual(merge_sort([3, 1, 4, 1, 5, 9, 2, 6]), [1, 1, 2, 3, 4, 5, 6, 9])

    # 测试包含重复元素的数组
    def test_array_with_duplicates(self):
        # 断言merge_sort([3, 3, 3])的结果为[3, 3, 3]
        self.assertEqual(merge_sort([3, 3, 3]), [3, 3, 3])

    # 测试包含负数的数组
    def test_array_with_negative_numbers(self):
        # 断言merge_sort([-1, -3, -2, -5, -4])的结果为[-5, -4, -3, -2, -1]
        self.assertEqual(merge_sort([-1, -3, -2, -5, -4]), [-5, -4, -3, -2, -1])

    # 测试包含正数和负数的混合数组
    def test_array_with_mixed_positive_and_negative_numbers(self):
        # 断言merge_sort([1, -2, 3, -4, 5])的结果为[-4, -2, 1, 3, 5]
        self.assertEqual(merge_sort([1, -2, 3, -4, 5]), [-4, -2, 1, 3, 5])


if __name__ == '__main__':
    unittest.main()


