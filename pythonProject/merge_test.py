import unittest
from MergeSort2 import merge

class TestMergeFunction(unittest.TestCase):

    def test_merge_empty_lists(self):
        """测试两个空列表合并"""
        self.assertEqual(merge([], []), [])

    def test_merge_left_empty(self):
        """测试左列表为空"""
        self.assertEqual(merge([], [1, 2, 3]), [1, 2, 3])

    def test_merge_right_empty(self):
        """测试右列表为空"""
        self.assertEqual(merge([1, 2, 3], []), [1, 2, 3])

    def test_merge_equal_length(self):
        """测试等长列表合并"""
        self.assertEqual(merge([1, 3, 5], [2, 4, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_unequal_length(self):
        """测试不等长列表合并"""
        self.assertEqual(merge([1, 3], [2, 4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_duplicate_elements(self):
        """测试包含重复元素的列表合并"""
        self.assertEqual(merge([1, 2, 2, 3], [2, 3, 4]), [1, 2, 2, 2, 3, 3, 4])

    def test_merge_all_left_smaller(self):
        """测试左列表所有元素都小于右列表"""
        self.assertEqual(merge([1, 2, 3], [4, 5, 6]), [1, 2, 3, 4, 5, 6])

    def test_merge_all_right_smaller(self):
        """测试右列表所有元素都小于左列表"""
        self.assertEqual(merge([4, 5, 6], [1, 2, 3]), [1, 2, 3, 4, 5, 6])

    def test_merge_single_element_lists(self):
        """测试单元素列表合并"""
        self.assertEqual(merge([1], [2]), [1, 2])
        self.assertEqual(merge([2], [1]), [1, 2])

    def test_merge_equal_element(self):
        """测试相同元素数组合并"""
        self.assertEqual(merge([3], [3, 3]), [3, 3, 3])

if __name__ == '__main__':
    unittest.main()