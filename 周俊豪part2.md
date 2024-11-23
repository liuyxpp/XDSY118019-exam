### 第一题

1）`find_name_value` 的主要功能是从一个数据目录名中提取变量名和变量值，并将它们作为一个元组（其中变量值为浮点型）返回，目录名的格式是 `<name><value>` ，如果是负值则在变量值后会有 `n` 表示。

2）编写测试函数如下，经过测试，函数功能实现如预期。

```python
def test_find_name_value():
    test_cases = [
        # 正常输入（正浮点数）
        ("phi0.1"),
        # 正常输入（整数）
        ("xN14"),
        # 正常输入（负浮点数，后缀 'n'）
        ("kappa0.5n"),
        # 正常输入（负整数，后缀 'n'）
        ("yN30n"),
        # 边界输入（仅变量名，无数值）
        ("alpha"),
        # 边界输入（数值为零）
        ("beta0"),
        # 异常输入（数值格式不正确）
        ("g2ammaabn"),
        # 异常输入（带有额外字符但没有数值）
        ("zeta-xyz_"),
        # 边界输入（空字符串）
        (""),
        # 异常输入（只有数值）
        ("20.5n"),
    ]

    for i, input_data in enumerate(test_cases):
        result = find_name_value(input_data)
        print(result)
```

输出如下

```
('phi', 0.1)
('xN', 14.0)
('kappa', -0.5)
('yN', -30.0)
('alpha', None)
('beta', 0.0)
('g', 2.0)
('zeta-xyz_', None)
('', None)
('', -20.5)
```

3）对于用下划线连接的文件名，原函数并不能正确解析，原函数仅能解析单个目录名，因此修改如下：

```python
def find_name_value(folder_name):
    '''Split the name of a data directory into a list of (name, value) tuples.

    The format of each segment in ``folder_name``:

        <name><value>

    If the value is negative, it should be followed by a 'n'.

    Args:
        folder_name (str): the name of a :term:`data directory`.

    Returns:
        list: A list of tuples, where each tuple contains:

            * name (str): variable name.
            * value (float): value of the variable.
    '''
    # 分割输入字符串
    segments = folder_name.split('_')
    results = []

    # 解析每个部分
    pattern = '([-+]?\d*\.\d+|[-+]?\d+)'
    for segment in segments:
        rst = re.split(pattern, segment)
        if len(rst) < 2:
            results.append((segment, None))
            continue
        name = rst[0]
        valuestr = rst[1]
        sign_str = ''
        if len(rst) > 2:
            sign_str = rst[2]
        if sign_str == 'n':
            value = '-' + valuestr
        else:
            value = valuestr

        results.append((name, float(value)))

    return results
```

运行后得到结果

```
[('phi', 0.1), ('xN', 14.2), ('kappa', -0.5)]
[('a', 1.0), ('b', -14.0), ('n', 0.0), ('c', 0.2)]
```

### 第二题

```matlab
R = 3;
r = 1;
theta = linspace(0, 2*pi, 100);
phi = linspace(0, 2*pi, 100);
[Theta, Phi] = meshgrid(theta, phi);

X = (R + r * cos(Theta)) .* cos(Phi);
Y = (R + r * cos(Theta)) .* sin(Phi);
Z = r * sin(Theta);

figure;
surf(X, Y, Z);
shading interp;
colormap jet;
axis equal;
xlabel('X');
ylabel('Y');
zlabel('Z');
title('Torus (环面)');

```

![matlat截图](.\2.jpg)

### 第三题

```mathematica
Sum[1/(n^3 + n^2), {n, 1, Infinity}]
```

结果为 $-1 + \frac{\pi^2}{6}$

```mathematica
Integrate[Sqrt[x] Log[x]/(x + 1)^2, {x, 0, Infinity}]
```

结果为 $\pi$

### 第四题

$\mathbf{Q}:$ $Find$ $the$ $solution$ $of$ $the$ $following$ $equation$ $with$ $respect$ $to$ $\theta$:
$$
A \cos \theta + B \sin \theta + C = 0
$$

$\mathbf{A}:$

$let$ $ x_1 = \cos \theta $ $and$ $ x_2 = \sin \theta $$,$ $then$ $the$ $solution$ $is$ $given$ $by$ $the$ $intersection$ $of$ $the$ $circle$ $and$ $the$ $line$$:$
$$
\begin{aligned}
x_1^2 + x_2^2 = 1 \\
A x_1 + B x_2 + C = 0    
\end{aligned}
$$
$We$ $reformulate$ $the$ $equations$ $in$ $a$ $parametric$ $form$$:$

$$
\begin{aligned}
|\mathbf{x}|^2 = 1 \\
\quad \mathbf{x}(t) = \mathbf{a} + t \mathbf{b}
\end{aligned}
$$

$where$ $ \mathbf{x} = (x_1, x_2) $$,$ $ \mathbf{a} = (0, -C/B) $$,$ $ \mathbf{b} = (-C/A, C/B) $$,$ $and$ $ t $ $is$ $a$ $parameter$$.$ $The$ $intersection$ $points$ $satisfy$ $the$ $following$ $equation$$:$

$$
|\mathbf{a} + t \mathbf{b}|^2 = 1
$$

$which$ $can$ $be$ $solved$ $for$ $ t $ $to$ $find$ $the$ $intersection$ $points$$:$

$$
t_{1, 2} = \frac{-\mathbf{a} \cdot \mathbf{b} \pm \sqrt{(\mathbf{a} \cdot \mathbf{b})^2 - |\mathbf{b}|^2 (|\mathbf{a}|^2 - 1)}}{|\mathbf{b}|^2}
$$