import pytest
import timeit
import random
from MergeSort2 import merge_sort_iterative, merge_sort_recursive

# 改为动态规模控制
sizes = [1000, 10000, 100000, 1000000]  # 新增规模控制列表
data_types = ["sorted", "random", "reverse"]
# 性能测试参数化配置
IMPLEMENTATIONS = [
    ("iterative", merge_sort_iterative),
    ("recursive", merge_sort_recursive)
]

# 重构后的数据配置生成逻辑
DATA_CONFIG = {
    f"{data_type}_{size}": (size, data_type)
    for size in sizes
    for data_type in data_types
}
def generate_test_data(size, data_type):
    """生成指定类型和大小的测试数据"""
    arr = list(range(size))
    if data_type == "sorted":
        return arr
    elif data_type == "reverse":
        return arr[::-1]
    elif data_type == "random":
        return random.sample(arr, size)
    return arr

# ... 保留generate_test_data函数 ...

@pytest.mark.parametrize("impl_name,sort_func", IMPLEMENTATIONS)
@pytest.mark.parametrize("data_key", DATA_CONFIG.keys())
def test_sort_performance(impl_name, sort_func, data_key, benchmark):
    """性能基准测试"""
    size, data_type = DATA_CONFIG[data_key]
    test_data = generate_test_data(size, data_type)

    # 调整分组名称显示逻辑
    benchmark.group = f"{data_type}-{size}"

    # 执行排序并测量时间
    result = benchmark(sort_func, test_data.copy())

    # 优化输出格式
    print(f"{impl_name:10} | {data_type:7} | {size:7} | 平均耗时: {benchmark.stats['mean']:.6f}s")