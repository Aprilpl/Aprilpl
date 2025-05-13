def bubble_sort(arr):
    """
    冒泡排序算法
    
    参数:
    arr -- 需要排序的列表
    
    返回:
    排序后的列表
    """
    n = len(arr)
    # 外层循环控制排序轮数
    for i in range(n):
        # 设置标志位，用于优化算法
        swapped = False
        
        # 内层循环负责比较和交换元素
        # 每一轮结束后，最大的元素会"冒泡"到末尾
        # 因此每轮比较的次数可以减少
        for j in range(0, n - i - 1):
            # 如果前一个元素大于后一个元素，则交换它们
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
                
        # 如果在某一轮中没有发生交换，说明数组已经有序，可以提前结束
        if not swapped:
            break
            
    return arr

# 测试冒泡排序函数
if __name__ == "__main__":
    # 测试用例1：随机顺序数组
    test_arr1 = [64, 34, 25, 12, 22, 11, 90]
    sorted_arr1 = bubble_sort(test_arr1.copy())
    print(f"排序前: {test_arr1}")
    print(f"排序后: {sorted_arr1}")
    
    # 测试用例2：已排序数组
    test_arr2 = [1, 2, 3, 4, 5]
    sorted_arr2 = bubble_sort(test_arr2.copy())
    print(f"\n排序前: {test_arr2}")
    print(f"排序后: {sorted_arr2}")
    
    # 测试用例3：逆序数组
    test_arr3 = [5, 4, 3, 2, 1]
    sorted_arr3 = bubble_sort(test_arr3.copy())
    print(f"\n排序前: {test_arr3}")
    print(f"排序后: {sorted_arr3}")
    
    # 测试用例4：包含重复元素的数组
    test_arr4 = [5, 2, 8, 5, 1, 3, 2]
    sorted_arr4 = bubble_sort(test_arr4.copy())
    print(f"\n排序前: {test_arr4}")
    print(f"排序后: {sorted_arr4}") 


