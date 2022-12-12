# 考拉兹序列的Python编程实现

#### 范旭涛 20307130179

查看实现效果，只需将文件末尾的函数的注释分别打开，运行文件，便可查看相应题目的实现。
```python
# 题目一：  
# print_collatz_sequence()  
# 题目二：  
# draw_collatz_graph()  
# 题目三：  
# draw_collatz_tree()
```

## 题目一：对于给定的数生成考拉兹序列

1. 现需要向用户获取所需的数n
```python
n = int(input("请输入希望求出考拉兹序列的值："))
```

2. 利用一个循环结构按照定义判断即可
```python
while n != 1:  
    sequence.append(n)  
    if n % 2:  
        n = n * 3 + 1  
    else:  
        n //= 2
sequence.append(1)  # 由于终止在n为1时，需要多加入1
```

3. 最后打印
```python
print(sequence)
```

## 题目二：对于给定的数组生成考拉兹序列收敛图

1. 利用1中的方法生成一系列考拉兹序列，也就是生成一个二位数组。其实可以将这个过程封装一下，但本来代码也不长，就不去麻烦了。
```python
num = [3 * i for i in range(1, 11)]  
sequence = []  # 考拉兹序列，存储成一个二维数组  
for i in range(0, len(num)):  
    sequence.append([])  
    while num[i] != 1:  # 尚未到达1，则继续循环  
        sequence[i].append(num[i])  
        if num[i] % 2:  
            num[i] = num[i] * 3 + 1  
        else:  
            num[i] //= 2  
    sequence[i].append(1)
```

2. 定义一个`myplot()`函数，其中根据`matplotlib.pyplot`库中的方法将多条折线图画在同一个二维平面上，这里用到了[week 7 lecture slide](https://github.com/liuyxpp/XDSY118019/blob/main/notebooks/04_python_plotting.ipynb )中的代码。其中x轴序列的生成，直接利用序列长度和`range()`方法生成，也就是`len(sequence[i])。
```python
def my_plot(sequence):  
    fig, ax = plt.subplots(1)  
    linestyles = mpltex.linestyle_generator()  
    for i in range(0, len(sequence)):  
        ax.plot(range(len(sequence[i])), sequence[i], label=str(sequence[i][0]), **next(linestyles))  
    ax.set_xlabel('$t$')  
    ax.set_ylabel('$f(t)$')  
    ax.legend(loc='best', ncol=1)  
    fig.tight_layout(pad=0.1)  
    # Uncomment following line to save the resulted figure as an EPS image file.  
    fig.savefig('mpltex-acs')  
    plt.show()
```

## 题目三：对于给定的起始值和最大值生成考拉兹分析树

不得不吐槽一句，python在写树的时候实在不是很方便，这主要在于：
1. 无法利用指针向函数传参
2. 函数不显示声明返回值，很容易让人一头雾水
3. 变量没有显示的声明类型，太模糊

下面还是回到正题，分析树的生成:
1. 获取起始值和最大值， 并生成根结点，调用`list_create_tree（）`生成树。
```python
def draw_collatz_tree():  
    n = int(input("请输入您想要分析的序列的最大数值: "))  
    i = int(input("请输入您想要分析的序列的根结点的值: "))  
    root = TreeNode(0)  
    root = list_create_tree(root, n, i)  
    draw(root)
```

2. 定义`TreeNode`结点类，其左右孩子是都是在考拉兹序列中它的predecessor，只是根据定义中不同的方式产生的这个节点。但是需要注意，右孩子定义为通过`n * 3 + 1`产生这个节点的predecessor。但不是对于每个数，都存在一个奇数`n`这么产生它，也就是，不是每个节点都有右孩子，下面几种情况就没有：
	1. 不存在这样一个奇数通过`n * 3 + 1`产生当前节点`i`。这种情况需要通过以下几条语句表述。
		- `(i - 1) / 3 == (i - 1) // 3`表明，这个n不是小数。
		- `(i - 1) // 3 > 0`表明，predecessor不能为0或负数。
		- `((i - 1) // 3) % 2`表明， 这整数`n`不是奇数。
	```python 
	(i - 1) / 3 == (i - 1) // 3 \  
        and (i - 1) // 3 > 0 \  
        and ((i - 1) // 3) % 2 \  
	```
	2. 这个奇数predecessor不能是1。
	```python
	and (i - 1) // 3 != 1:
	```

3. 利用`list_create_tree()`函数递归的构建数，递归基为一个节点大于等于给定的最大值时。
```python
def list_create_tree(root, n, i):  
    if i < n:  
        root = TreeNode(i)  
        if (i - 1) / 3 == (i - 1) // 3 \  
                and (i - 1) // 3 > 0 \  
                and ((i - 1) // 3) % 2 \  
                and (i - 1) // 3 != 1:  
            root.right = list_create_tree(root.right, n, (i - 1) // 3)  
        else:  
            root_right = None  
        root.left = list_create_tree(root.left, n, 2 * i)  
        return root  
    return root
```
4. 最后画图，这个两个函数参考了[Python 实现二叉树，并可视化](https://zhuanlan.zhihu.com/p/35574577)。
```python
def create_graph(G, node, pos={}, x=0, y=0, layer=1):  
    pos[node.value] = (x, y)  
    if node.left:  
        G.add_edge(node.value, node.left.value)  
        l_x, l_y = x - 1 / 2 ** layer, y - 1  
        l_layer = layer + 1  
        create_graph(G, node.left, x=l_x, y=l_y, pos=pos, layer=l_layer)  
    if node.right:  
        G.add_edge(node.value, node.right.value)  
        r_x, r_y = x + 1 / 2 ** layer, y - 1  
        r_layer = layer + 1  
        create_graph(G, node.right, x=r_x, y=r_y, pos=pos, layer=r_layer)  
    return G, pos  
  
  
# 以某个节点为根画图  
def draw(node):  
    graph = nx.DiGraph()  
    graph, pos = create_graph(graph, node)  
    fig, ax = plt.subplots(figsize=(8, 8))  # 比例可以根据树的深度适当调节  
    nx.draw_networkx(graph, pos, ax=ax, node_size=300)  
    plt.show()
```