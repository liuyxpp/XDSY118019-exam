import numpy as np

def matrix_stats(mat):
    arr = np.array(mat)

    if arr.size == 0:
        return {
            'max': np.nan,
            'min': np.nan,
            'mean': np.nan,
            'std': np.nan,
            'sr': np.nan,
            'sum': 0 
        }
    
    # 还要避免除数为0
    max = np.max(arr)
    min = np.min(arr)
    mean = np.mean(arr)
    std = np.std(arr)
    sum = np.sum(arr)

    if std == 0:
        sr = np.inf if mean != 0 else np.nan
    else:
        sr = mean / std

    return {
        'max':max,
        'min': min,
        'mean': mean,
        'std': std,
        'sr': sr,
        'sum':sum
    }

if __name__ == '__main__':
    print("求A")
    A = [[1,2,3],[4,5,6]]
    resultA = matrix_stats(A)
    print(resultA)

    print("求B")
    B = [[-1,0],[0,1]]
    resultB = matrix_stats(B)
    print(resultB)

    # 以下是测试
    print("测试1: 正常3x3矩阵")
    matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    result1 = matrix_stats(matrix1)
    print(f"结果: {result1}")
    
    print("测试2: 单元素矩阵")
    matrix2 = [[5]]
    result2 = matrix_stats(matrix2)
    print(f"结果: {result2}")
    
    print("测试3: 空矩阵")
    matrix3 = []
    result3 = matrix_stats(matrix3)
    print(f"结果: {result3}")
    
    # 测试4: 包含负数的矩阵
    print("测试4: 包含负数的矩阵")
    matrix4 = [[-1, -2], [0, 1]]
    result4 = matrix_stats(matrix4)
    print(f"结果: {result4}")
    
    # 测试5: 常数矩阵
    print("测试5: 常数矩阵")
    matrix5 = [[3, 3], [3, 3]]
    result5 = matrix_stats(matrix5)
    print(f"结果: {result5}")