import numpy as np

def matrix_stats(mat):
    arr = np.array(mat)
    mean_val = np.mean(arr)
    std_val = np.std(arr)
    
    if std_val == 0:
        sr_val = np.nan if mean_val == 0 else (np.inf if mean_val > 0 else -np.inf)
    else:
        sr_val = mean_val / std_val
    
    return {
        'max': np.max(arr),
        'min': np.min(arr),
        'mean': mean_val,
        'std': std_val,
        'sr': sr_val,
        'sum': np.sum(arr),
    }

if __name__ == '__main__':
    
    A = np.array([[1, 2, 3], [4, 5, 6]])
    B = np.array([[-1, 0], [0, 1]])
    
    print(f"matrix_stats(A): {matrix_stats(A)}")
    print(f"matrix_stats(B): {matrix_stats(B)}")

    # Test Case 1: 正常输入
    C1 = [[1, 2, 3], [4, 5, 6]]
    print(f"matrix_stats(C1): {matrix_stats(C1)}")
    
    # Test Case 2: 正常输入 - 包含负数和零
    C2 = [[-5, -3, 0], [2, 4, 8]]
    print(f"matrix_stats(C2): {matrix_stats(C2)}")

    # Test Case 3: 正常输入 - 浮点数矩阵
    C3 = [[1.5, 2.5], [3.5, 4.5]]
    print(f"matrix_stats(C3): {matrix_stats(C3)}")

    # Test Case 4: 边界输入 - 单个元素矩阵(1x1)
    C4 = [[42]]
    print(f"matrix_stats(C4): {matrix_stats(C4)}")
    
    # Test Case 5: 边界输入 - 一维矩阵
    C5 = [1, 2, 3, 4, 5]
    print(f"matrix_stats(C5): {matrix_stats(C5)}")

    # Test Case 6: 异常输入 - 空矩阵
    C6 = []
    try:
        print(f"matrix_stats(C6): {matrix_stats(C6)}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    
    # Test Case 7: 异常输入 - 不规则矩阵
    C7 = [[1, 2], [3, 4, 5], [6]]
    try:
        print(f"matrix_stats(C7): {matrix_stats(C7)}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    
