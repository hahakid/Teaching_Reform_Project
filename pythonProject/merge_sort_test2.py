import pytest
from MergeSort2 import merge_sort_iterative

def test_merge_sort_iterative_empty_list():
    """测试空列表"""
    assert merge_sort_iterative([]) == []

def test_merge_sort_iterative_single_element():
    """测试单元素列表"""
    assert merge_sort_iterative([5]) == [5]

def test_merge_sort_iterative_sorted_list():
    """测试已排序列表"""
    assert merge_sort_iterative([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_merge_sort_iterative_reverse_sorted():
    """测试逆序列表"""
    assert merge_sort_iterative([4, 3, 2, 1]) == [1, 2, 3, 4]

def test_merge_sort_iterative_random_order():
    """测试随机顺序列表"""
    assert merge_sort_iterative([3, 1, 4, 2]) == [1, 2, 3, 4]

def test_merge_sort_iterative_duplicate_elements():
    """测试包含重复元素的列表"""
    assert merge_sort_iterative([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

def test_merge_sort_iterative_odd_length():
    """测试奇数长度列表"""
    assert merge_sort_iterative([5, 3, 1, 4, 2]) == [1, 2, 3, 4, 5]

def test_merge_sort_iterative_large_list():
    """测试大型列表"""
    import random
    arr = [random.randint(0, 1000) for _ in range(1000)]
    assert merge_sort_iterative(arr.copy()) == sorted(arr)

def test_merge_sort_iterative_negative_numbers():
    """测试包含负数的列表"""
    assert merge_sort_iterative([-3, 1, -2, 4, 0]) == [-3, -2, 0, 1, 4]