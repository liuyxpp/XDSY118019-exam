import numpy as np

def matrix_stats(mat):
    arr = np.array(mat)
    return {
        'max': np.max(arr),
        'min': np.min(arr),
        'mean': np.mean(arr),
        'std': np.std(arr),
        'sr': np.mean(arr) / np.std(arr)
    }

if __name__ == '__main__':
    pass