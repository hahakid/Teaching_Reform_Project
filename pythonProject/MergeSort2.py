# Trae

def merge_sort_recursive(arr):
    """递归实现（自顶向下）"""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort_recursive(arr[:mid])
    right = merge_sort_recursive(arr[mid:])
    return merge(left, right)

def merge_sort_iterative(arr):
    """迭代实现（自底向上）"""
    n = len(arr)
    size = 1

    while size < n:
        for i in range(0, n, size * 2):
            left = i
            mid = i + size
            right = min(i + 2 * size, n)

            # 获取当前要合并的两个子数组
            left_arr = arr[left:mid]
            right_arr = arr[mid:right]

            # 执行合并并替换原数组对应位置
            merged = merge(left_arr, right_arr)
            arr[left:right] = merged

        size *= 2
    return arr

def merge(left, right):
    """通用合并函数"""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result














