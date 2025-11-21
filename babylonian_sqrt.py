"""
巴比伦平方根算法实现

这个文件实现了巴比伦方法来计算平方根，
包括两种不同的误差定义方式，还有收敛性分析。
"""

import numpy as np
import matplotlib.pyplot as plt
from typing import Tuple, List


def babylonian(y: float, epsilon: float, x0: float = 1.0) -> Tuple[float, int, float]:
    """
    用巴比伦方法计算 y 的平方根。
    
    算法就是不断迭代这个公式：
        x_{n+1} = 0.5 * (x_n + y / x_n)
    
    当误差 |x_n - sqrt(y)| < epsilon 时就停止。
    
    参数:
        y: 要算平方根的数，必须是正数
        epsilon: 误差阈值，必须是正数
        x0: 初始猜测值，默认是 1.0，必须是正数
    
    返回:
        返回三个值：
            - x_n: 算出来的平方根近似值
            - n: 迭代了多少次
            - epsilon_n: 真实误差是多少
    
    异常:
        如果输入不是正数会报错
    """
    # 先检查输入是否合法
    if y <= 0:
        raise ValueError("y must be positive")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    if x0 <= 0:
        raise ValueError("x0 must be positive")
    
    # 用 numpy 算出真实值，用来计算误差
    true_sqrt = np.sqrt(y)
    
    # 初始化，从 x0 开始
    x_n = x0
    n = 0
    epsilon_n = abs(x_n - true_sqrt)
    
    # 不断迭代，直到误差满足要求
    while epsilon_n >= epsilon:
        # 应用巴比伦公式
        x_n = 0.5 * (x_n + y / x_n)
        n += 1
        epsilon_n = abs(x_n - true_sqrt)
        
        # 防止程序卡死，设置最大迭代次数
        if n > 10000:
            raise RuntimeError(f"Algorithm did not converge after {n} iterations")
    
    return x_n, n, epsilon_n


def analyze_convergence(y: float, epsilon_values: List[float], x0: float = 1.0) -> None:
    """
    画图分析收敛行为，看误差怎么随迭代次数变化。
    
    这个函数会测试不同的误差阈值，然后画出收敛曲线。
    
    参数:
        y: 要算平方根的数
        epsilon_values: 要测试的误差阈值列表
        x0: 初始猜测值，默认是 1.0
    """
    true_sqrt = np.sqrt(y)
    plt.figure(figsize=(10, 6))
    
    for epsilon in epsilon_values:
        # 记录每次迭代的误差
        errors = []
        x_n = x0
        n = 0
        epsilon_n = abs(x_n - true_sqrt)
        
        # 迭代直到收敛
        while epsilon_n >= epsilon:
            errors.append(epsilon_n)
            x_n = 0.5 * (x_n + y / x_n)
            n += 1
            epsilon_n = abs(x_n - true_sqrt)
            
            # 防止卡死
            if n > 10000:
                break
        
        # 画图，用对数坐标
        iterations = range(len(errors))
        plt.semilogy(iterations, errors, marker='o', label=f'ε = {epsilon:.0e}', markersize=4)
    
    plt.xlabel('Iteration Number (n)', fontsize=12)
    plt.ylabel('Error (ε_n)', fontsize=12)
    plt.title(f'Convergence Analysis: Error vs Iteration (y = {y}, x0 = {x0})', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('convergence_analysis.png', dpi=300, bbox_inches='tight')
    plt.close()  # 关闭图形，避免内存问题
    print("Convergence analysis plot saved as 'convergence_analysis.png'")


def analyze_initial_value_impact(y: float, epsilon: float, x0_values: List[float]) -> None:
    """
    分析不同的初始值 x0 对收敛有什么影响。
    
    这个函数会测试不同的初始值，然后画图看看哪个收敛更快。
    
    参数:
        y: 要算平方根的数
        epsilon: 误差阈值
        x0_values: 要测试的初始值列表
    """
    true_sqrt = np.sqrt(y)
    plt.figure(figsize=(10, 6))
    
    for x0 in x0_values:
        # 记录每次迭代的误差
        errors = []
        x_n = x0
        n = 0
        epsilon_n = abs(x_n - true_sqrt)
        
        # 迭代直到收敛
        while epsilon_n >= epsilon:
            errors.append(epsilon_n)
            x_n = 0.5 * (x_n + y / x_n)
            n += 1
            epsilon_n = abs(x_n - true_sqrt)
            
            # 防止卡死
            if n > 10000:
                break
        
        # 画图
        iterations = range(len(errors))
        plt.semilogy(iterations, errors, marker='o', label=f'x0 = {x0}', markersize=4)
    
    plt.xlabel('Iteration Number (n)', fontsize=12)
    plt.ylabel('Error (ε_n)', fontsize=12)
    plt.title(f'Impact of Initial Value x0 on Convergence (y = {y}, ε = {epsilon:.0e})', fontsize=14)
    plt.legend()
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('initial_value_impact.png', dpi=300, bbox_inches='tight')
    plt.close()  # 关闭图形，避免内存问题
    print("Initial value impact analysis plot saved as 'initial_value_impact.png'")


def babylonian2(y: float, epsilon: float = 1e-10, x0: float = 1.0) -> Tuple[np.ndarray, np.ndarray]:
    """
    用另一种误差定义来计算平方根。
    
    这个版本用相邻两次迭代的差值来判断是否收敛：
    ε_n = |x_{n+1} - x_n|
    当这个差值小于 epsilon 时就停止。
    
    参数:
        y: 要算平方根的数，必须是正数
        epsilon: 误差阈值，默认是 1e-10，必须是正数
        x0: 初始猜测值，默认是 1.0，必须是正数
    
    返回:
        返回两个数组：
            - x_array: 每次迭代的值
            - epsilon_array: 每次迭代的误差（相邻两次的差值）
    """
    # 检查输入
    if y <= 0:
        raise ValueError("y must be positive")
    if epsilon <= 0:
        raise ValueError("epsilon must be positive")
    if x0 <= 0:
        raise ValueError("x0 must be positive")
    
    # 保存所有迭代的值
    x_array = [x0]
    epsilon_array = []
    
    x_n = x0
    n = 0
    
    # 迭代直到收敛
    while True:
        # 计算下一次迭代
        x_next = 0.5 * (x_n + y / x_n)
        
        # 计算相邻两次迭代的差值
        epsilon_n = abs(x_next - x_n)
        epsilon_array.append(epsilon_n)
        
        # 如果差值很小，说明已经收敛了
        if epsilon_n < epsilon:
            x_array.append(x_next)
            break
        
        x_array.append(x_next)
        x_n = x_next
        n += 1
        
        # 防止卡死
        if n > 10000:
            raise RuntimeError(f"Algorithm did not converge after {n} iterations")
    
    return np.array(x_array), np.array(epsilon_array)


def analyze_convergence2(y: float, epsilon: float = 1e-10, x0: float = 1.0) -> None:
    """
    用替代误差定义来分析收敛行为。
    
    这个函数会画出相邻迭代误差随迭代次数变化的图。
    
    参数:
        y: 要算平方根的数
        epsilon: 误差阈值，默认是 1e-10
        x0: 初始猜测值，默认是 1.0
    """
    x_array, epsilon_array = babylonian2(y, epsilon, x0)
    
    plt.figure(figsize=(10, 6))
    iterations = range(len(epsilon_array))
    plt.semilogy(iterations, epsilon_array, marker='o', markersize=4)
    
    plt.xlabel('Iteration Number (n)', fontsize=12)
    plt.ylabel('Error (ε_n = |x_{n+1} - x_n|)', fontsize=12)
    plt.title(f'Convergence Analysis: Alternative Error Definition (y = {y}, x0 = {x0}, ε = {epsilon:.0e})', fontsize=14)
    plt.grid(True, alpha=0.3)
    plt.tight_layout()
    plt.savefig('convergence_analysis2.png', dpi=300, bbox_inches='tight')
    plt.close()  # 关闭图形，避免内存问题
    print("Alternative convergence analysis plot saved as 'convergence_analysis2.png'")


def main():
    """
    主函数，运行所有测试和分析。
    """
    # 用 25 来测试，因为它的平方根是 5，比较好验证
    y = 25.0
    
    print("=" * 60)
    print("巴比伦平方根算法 - 演示")
    print("=" * 60)
    
    # 测试第一个函数
    print("\n1. 测试 babylonian() 函数:")
    result = babylonian(y, 1e-10)
    print(f"   y = {y}")
    print(f"   近似平方根: {result[0]:.15f}")
    print(f"   真实平方根: {np.sqrt(y):.15f}")
    print(f"   迭代次数: {result[1]}")
    print(f"   最终误差: {result[2]:.2e}")
    
    # 测试不同误差阈值
    print("\n2. 分析不同 epsilon 值的收敛性...")
    epsilon_values = [1e-1, 1e-2, 1e-3, 1e-4, 1e-5, 1e-6, 1e-7, 1e-8, 1e-9, 1e-10, 1e-11, 1e-12, 1e-13, 1e-14, 1e-15]
    analyze_convergence(y, epsilon_values)
    
    # 测试不同初始值
    print("\n3. 分析不同初始值 x0 的影响...")
    x0_values = [0.1, 0.5, 1.0, 2.0, 5.0, 10.0, 20.0, 50.0]
    analyze_initial_value_impact(y, 1e-10, x0_values)
    
    # 测试第二个函数
    print("\n4. 使用替代误差定义测试 babylonian2() 函数:")
    x_arr, eps_arr = babylonian2(y, 1e-10)
    print(f"   最终值: {x_arr[-1]:.15f}")
    print(f"   真实平方根: {np.sqrt(y):.15f}")
    print(f"   迭代次数: {len(eps_arr)}")
    print(f"   最终误差: {eps_arr[-1]:.2e}")
    
    # 分析替代误差定义的收敛性
    print("\n5. 使用替代误差定义分析收敛性...")
    analyze_convergence2(y, 1e-10)
    
    print("\n" + "=" * 60)
    print("All analyses completed!")
    print("=" * 60)


if __name__ == "__main__":
    main()

