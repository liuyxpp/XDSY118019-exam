# 巴比伦平方根算法实现

## 问题描述

这次作业要求实现巴比伦平方根算法。这个算法很古老，是古巴比伦人用来计算平方根的方法。算法的核心公式是：

$$x_{n+1} = \frac{1}{2}\left(x_n + \frac{y}{x_n}\right)$$

简单来说，就是从某个初始猜测值 $x_0$ 开始，不断用这个公式迭代，最终会收敛到 $\sqrt{y}$。

### 误差定义

题目要求实现两种误差定义方式：

1. **真实误差**：$\epsilon_n = |x_n - \sqrt{y}|$
   - 就是看当前猜测值和真实值差多少
   - 当误差小于设定值时就停止
   - 我用在了 `babylonian()` 函数里

2. **相邻迭代误差**：$\varepsilon_n = |x_{n+1} - x_n|$
   - 看相邻两次迭代的结果差多少
   - 如果两次结果很接近，说明已经收敛了
   - 我用在了 `babylonian2()` 函数里

## 解答思路

### 1. 算法实现

我按照题目要求实现了算法：
- 首先检查输入是否合法（y、epsilon、x0 都要是正数）
- 然后按照公式进行迭代计算
- 每次迭代后检查误差，如果满足条件就停止
- 为了防止程序卡死，我还设置了最大迭代次数限制

### 2. 收敛性分析

为了理解算法的收敛行为，我做了以下分析：
- 画了误差随迭代次数变化的曲线，发现误差下降得很快（指数衰减）
- 测试了不同的初始值，发现初始值会影响收敛速度，但不影响最终结果
- 对比了两种误差定义，发现它们都能有效判断收敛

### 3. 可视化分析

我用 `matplotlib` 画了几张图来帮助理解：
- 不同误差阈值下的收敛曲线（可以看到误差阈值越小，需要更多迭代）
- 不同初始值下的收敛曲线对比（可以看到初始值对收敛速度的影响）
- 两种误差定义下的收敛行为对比

## 如何使用代码

### 环境要求

运行前需要安装 numpy 和 matplotlib：

```bash
pip install numpy matplotlib
```

### 基本使用

#### 1. 使用 `babylonian()` 函数

这是第一个函数，用真实误差来判断收敛：

```python
from babylonian_sqrt import babylonian

# 计算 25 的平方根
result = babylonian(25.0, 1e-10, x0=1.0)

# 返回三个值：近似值、迭代次数、真实误差
sqrt_approx, iterations, error = result
print(f"平方根近似值: {sqrt_approx}")
print(f"迭代次数: {iterations}")
print(f"真实误差: {error}")
```

#### 2. 使用 `babylonian2()` 函数

这是第二个函数，用相邻迭代误差来判断收敛：

```python
from babylonian_sqrt import babylonian2

# 使用另一种误差定义
x_array, epsilon_array = babylonian2(25.0, epsilon=1e-10, x0=1.0)

# x_array 是每次迭代的值
# epsilon_array 是每次迭代的误差
print(f"最终值: {x_array[-1]}")
print(f"最终误差: {epsilon_array[-1]}")
```

#### 3. 运行完整分析

直接运行主程序就可以了：

```bash
python babylonian_sqrt.py
```

运行后会：
- 在控制台显示测试结果
- 生成三张图片：
  - `convergence_analysis.png`：不同误差阈值下的收敛曲线
  - `initial_value_impact.png`：不同初始值对收敛的影响
  - `convergence_analysis2.png`：使用替代误差定义的收敛曲线

#### 4. 自定义分析

如果想自己测试不同的参数，可以这样：

```python
from babylonian_sqrt import analyze_convergence, analyze_initial_value_impact, analyze_convergence2

# 测试不同的误差阈值
epsilon_values = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5]
analyze_convergence(25.0, epsilon_values, x0=1.0)

# 测试不同的初始值
x0_values = [0.1, 1.0, 5.0, 10.0, 50.0]
analyze_initial_value_impact(25.0, 1e-10, x0_values)

# 用替代误差定义分析
analyze_convergence2(25.0, 1e-10, x0=1.0)
```

## 代码结构

我实现了以下几个函数：
- `babylonian()`: 基本算法，用真实误差判断收敛
- `analyze_convergence()`: 画不同误差阈值下的收敛曲线
- `analyze_initial_value_impact()`: 分析初始值对收敛的影响
- `babylonian2()`: 用相邻迭代误差判断收敛的版本
- `analyze_convergence2()`: 画替代误差定义的收敛曲线
- `main()`: 主函数，运行所有测试和分析

## 结果分析

### 1. 误差与迭代次数的关系

从画的图可以看出：
- 误差下降得很快，基本是指数衰减
- 误差阈值设得越小，需要更多次迭代
- 不过收敛速度还是挺快的，一般 10 次以内就能达到很高的精度

### 2. 初始值 $x_0$ 的影响

我测试了不同的初始值，发现：
- 不管初始值是多少（只要是正数），算法都能收敛到正确答案
- 如果初始值选得接近真实值，收敛会更快
- 算法对初始值不太敏感，所以选什么初始值都可以

### 3. 两种误差定义的比较

- **真实误差**：直接看和真实值差多少，但需要知道真实值（实际应用中可能不知道）
- **相邻迭代误差**：只需要看两次迭代的结果，更实用，但可能在某些情况下会提前停止

## 注意事项

使用代码时要注意：
1. 输入值 y 必须是正数
2. 误差阈值 epsilon 必须是正数
3. 初始值 x0 必须是正数
4. 对于 64 位浮点数，误差阈值最好不要超过 $10^{-15}$，因为会受到机器精度的限制
