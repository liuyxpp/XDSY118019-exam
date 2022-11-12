import mpltex
import networkx as nx
import matplotlib.pyplot as plt


# 为构建考拉兹数建立的节点
class TreeNode:
    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# 递归建立考拉兹树
#
# 对于一个数字，它的左孩子是它的两倍，
# 也就是左孩子在考拉兹序列中的后一位是它的父节点
# 对于另一种生成方式，也就是右孩子，
# 不过有右孩子不一定存在
#
# 传入的参数中 n 是最大结点的值，i是这一层结点的值
def list_create_tree(root, n, i):
    if i < n:
        root = TreeNode(i)
        if (i - 1) / 3 == (i - 1) // 3 \
                and (i - 1) // 3 > 0 \
                and ((i - 1) // 3) % 2 \
                and (i - 1) // 3 != 1:
            root.right = list_create_tree(root.right, n, (i - 1) // 3)  # 如果存在右孩子便赋值
        else:
            root_right = None
        root.left = list_create_tree(root.left, n, 2 * i)  # 左孩子一定存在
        return root
    return root


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


# 绘制考拉兹树
def draw_collatz_tree():
    n = int(input("请输入您想要分析的序列的最大数值: "))
    i = int(input("请输入您想要分析的序列的根结点的值: "))
    root = TreeNode(0)
    root = list_create_tree(root, n, i)
    draw(root)


# 绘制某个考拉兹序列收敛图
def my_plot(sequence):
    fig, ax = plt.subplots(1)
    linestyles = mpltex.linestyle_generator()
    for i in range(0, len(sequence)):
        ax.plot(range(len(sequence[i])), sequence[i], label=str(sequence[i][0]), **next(linestyles)) # 根据序列长度生成x轴
    ax.set_xlabel('$t$')
    ax.set_ylabel('$f(t)$')
    ax.legend(loc='best', ncol=1)
    fig.tight_layout(pad=0.1)
    # Uncomment following line to save the resulted figure as an EPS image file.
    fig.savefig('mpltex-acs')
    plt.show()


# 绘制题目要求的考拉兹序列收敛图
def draw_collatz_graph():
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
    my_plot(sequence)


def print_collatz_sequence():
    n = int(input("请输入希望求出考拉兹序列的值："))
    sequence = []
    while n != 1:
        sequence.append(n)
        if n % 2:
            n = n * 3 + 1
        else:
            n //= 2
    sequence.append(1)  # 由于终止在n为1时，需要多加入1
    print("对应的考拉兹序列是: ", end="")
    print(sequence)


# 题目一：
# print_collatz_sequence()
# 题目二：
# draw_collatz_graph()
# 题目三：
# draw_collatz_tree()
