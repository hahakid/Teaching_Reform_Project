import time
import random
from memory_profiler import memory_usage
from MergeSort2 import merge_sort_recursive, merge_sort_iterative


def generate_test_data(size, case_type):
    """生成不同特征的测试数据"""
    if case_type == 'random':
        return [random.randint(-10000, 10000) for _ in range(size)]
    elif case_type == 'sorted':
        return sorted([random.randint(-10000, 10000) for _ in range(size)])
    elif case_type == 'reverse_sorted':
        return sorted([random.randint(-10000, 10000) for _ in range(size)], reverse=True)
    return []


def performance_test():
    """性能测试主函数"""
    test_cases = {
        'random': 100000,  # 10万随机数
        'sorted': 100000,  # 10万已排序数
        'reverse_sorted': 100000  # 10万逆序数
    }

    for case_type, size in test_cases.items():
        # 生成测试数据
        data = generate_test_data(size, case_type)

        # 时间复杂度测试
        start = time.perf_counter()
        merge_sort_iterative(data.copy())
        elapsed = time.perf_counter() - start

        # 时间复杂度测试
        start = time.perf_counter()
        merge_sort_recursive(data.copy())
        elapsed2 = time.perf_counter() - start

        # 空间复杂度测试
        mem_usage = max(memory_usage((merge_sort_iterative, (data.copy(),))))
        mem_usage2 = max(memory_usage((merge_sort_recursive, (data.copy(),))))


        print(f"\n测试类型: {case_type} (规模: {size})")
        print(f"merge_sort_iterative:")

        print(f"耗时: {elapsed:.4f}秒")
        print(f"峰值内存: {mem_usage:.2f} MiB")

        print(f"merge_sort_recursive:")
        print(f"耗时: {elapsed2:.4f}秒")
        print(f"峰值内存: {mem_usage2:.2f} MiB")


# 在测试代码块中添加
if __name__ == "__main__":
    # ... 原有测试代码 ...

    # 性能测试
    print("\n性能测试结果:")
    performance_test()