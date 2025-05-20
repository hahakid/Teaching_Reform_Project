import unittest
from MergeSort2 import merge_sort_recursive


class TestMergeSortRecursive(unittest.TestCase):
    # 测试空列表的情况
    def test_empty_list(self):
        # 断言merge_sort_recursive([])的结果应该是[]
        self.assertEqual(merge_sort_recursive([]), [])

    # 测试只有一个元素的列表
    def test_single_element(self):
        # 断言merge_sort_recursive([5])的结果应该是[5]
        self.assertEqual(merge_sort_recursive([5]), [5])
        self.assertEqual(merge_sort_recursive([3, 3, 3]), [3, 3, 3])


    # 测试已经排序好的列表
    def test_sorted_list(self):
        # 断言merge_sort_recursive([1, 2, 3, 4])的结果应该是[1, 2, 3, 4]
        self.assertEqual(merge_sort_recursive([1, 2, 3, 4]), [1, 2, 3, 4])

    # 测试逆序排序的列表
    def test_reverse_sorted_list(self):
        # 断言merge_sort_recursive([4, 3, 2, 1])的结果应该是[1, 2, 3, 4]
        self.assertEqual(merge_sort_recursive([4, 3, 2, 1]), [1, 2, 3, 4])

    # 测试包含重复元素的列表
    def test_duplicate_elements(self):
        # 断言merge_sort_recursive([3, 1, 2, 1, 3])的结果应该是[1, 1, 2, 3, 3]
        self.assertEqual(merge_sort_recursive([3, 1, 2, 1, 3]), [1, 1, 2, 3, 3])

    # 测试奇数长度的列表
    def test_odd_length_list(self):
        # 断言merge_sort_recursive([5, 2, 8, 1, 3])的结果应该是[1, 2, 3, 5, 8]
        self.assertEqual(merge_sort_recursive([5, 2, 8, 1, 3]), [1, 2, 3, 5, 8])

    # 测试偶数长度的列表
    def test_even_length_list(self):
        # 断言merge_sort_recursive([6, 4, 2, 1, 3, 5])的结果应该是[1, 2, 3, 4, 5, 6]
        self.assertEqual(merge_sort_recursive([6, 4, 2, 1, 3, 5]), [1, 2, 3, 4, 5, 6])

    # 测试包含负数的列表
    def test_negative_numbers(self):
        # 断言merge_sort_recursive([-3, -1, -2, -4])的结果应该是[-4, -3, -2, -1]
        self.assertEqual(merge_sort_recursive([-3, -1, -2, -4]), [-4, -3, -2, -1])

    # 测试包含正数和负数的混合列表
    def test_mixed_numbers(self):
        # 调用merge_sort_recursive函数对列表[0, -1, 2, -3, 4]进行排序
        # 预期结果是[-3, -1, 0, 2, 4]，即从小到大排序
        self.assertEqual(merge_sort_recursive([0, -1, 2, -3, 4]), [-3, -1, 0, 2, 4])


if __name__ == '__main__':
    unittest.main()