# 1.

## i.

```python
import numpy as np

def matrix_stats(mat):
    arr = np.array(mat)
    return {
        'max': float(np.max(arr)),
        'min': float(np.min(arr)),
        'mean': float(np.mean(arr)),
        'std': float(np.std(arr)),
        'sr': float(np.mean(arr)) / float(np.std(arr)),
        'sum': float(np.sum(arr))
    }

if __name__ == '__main__':
    pass
```
以上为修改后的代码

## ii.

### A

'max': 6.0

'min': 1.0

'mean': 3.5

'std': 1.707825127659933

'sr': 2.04939015319192

'sum': 21.0

### B

'max': 1.0

'min': -1.0

'mean': 0.0

'std': 0.7071067811865476

'sr': 0.0

'sum': 0.0

## iii.
问题1：要求输出数据为整数或浮点数，而原程序输出会显示`np.float64` `np.int64`，因此将这些数据统一改为浮点数来输出。**（已修改）**

问题2：若所有元素相同，`np.std(arr) = 0`，则计算`'sr'`时会报错，因此要分情况，若有`np.std(arr) = 0`，则不输出`'sr'`。

测试用例：

**正常输入1：**
$\begin{pmatrix}
1 & 2 & 3 \\ 4 & 5 & 6 \\7 & 8 & 9
\end{pmatrix}$

结果：`{'max': 9.0,
'min': 1.0,
'mean': 5.0,
'std': 2.581988897471611,
'sr': 1.9364916731037085,
'sum': 45.0}`

**正常输入2：**
$\begin{pmatrix}
1 & 2
\end{pmatrix}$

结果：`{'max': 2.0, 'min': 1.0, 'mean': 1.5, 'std': 0.5, 'sr': 3.0, 'sum': 3.0}`

**正常输入3：**
$\begin{pmatrix}
1 \\ 2
\end{pmatrix}$

结果：`{'max': 2.0, 'min': 1.0, 'mean': 1.5, 'std': 0.5, 'sr': 3.0, 'sum': 3.0}`

**边界输入：**
$\begin{pmatrix}
1
\end{pmatrix}$

结果：`ZeroDivisionError: float division by zero`

**异常输入：**
$\begin{pmatrix}
1 & 1 & 1 \\ 1 & 1
\end{pmatrix}$

结果：`setting an array element with a sequence. The requested array has an inhomogeneous shape after 1 dimensions. The detected shape was (2,) + inhomogeneous part.`

全部修改完的代码和示例：
```python
import numpy as np

def matrix_stats(mat):
    arr = np.array(mat)
    if float(np.std(arr)) != 0:
        return {
            'max': float(np.max(arr)),
            'min': float(np.min(arr)),
            'mean': float(np.mean(arr)),
            'std': float(np.std(arr)),
            'sr': float(np.mean(arr)) / float(np.std(arr)),
            'sum': float(np.sum(arr))
        }
    else:
        return {
            'max': float(np.max(arr)),
            'min': float(np.min(arr)),
            'mean': float(np.mean(arr)),
            'std': float(np.std(arr)),
            'sum': float(np.sum(arr))
        }

if __name__ == '__main__':
    print(matrix_stats([[1,2,3],[4,5,6],[7,8,9]]))
    print(matrix_stats([[1,2]]))
    print(matrix_stats([[1],[2]]))
    print(matrix_stats([[1]])) #边界
    print(matrix_stats([[1,1,1],[1,1]])) #异常,会报错
```

# 2.
Matlab命令：
```matlab
R = 3;
r = 0.7;

u = linspace(-r, r, 50);
v = linspace(0, 2*pi, 50);

[U, V] = meshgrid(u, v);

X = (R + U .* cos(V .* 0.5)) .* cos(V);
Y = (R + U .* cos(V .* 0.5)) .* sin(V);
Z = U .* sin(V .* 0.5);

figure;
surf(X, Y, Z);
```

图形：
![Mobius Strip](.\Figure_1.png)

# 3.

## i.
答案：-0.948855
![显示界面](.\Figure_2.png)

## ii.
答案：0.506671
![显示界面](.\Figure_3.png)

# 4
由于较复杂，直接用LaTeX写好后渲染在pdf里了
