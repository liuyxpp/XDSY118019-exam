范旭涛 20307130179
### Question 1.
**code:**
```python
temp = np.random.uniform(-2, 2, 95)  
test_num = np.append(temp, [-2, -1, 0, 1, 2]) # 构建100个测试数据，其中前95个是-2到2的小数，后5个是-2，-1，0，1，2  
test_decimals = np.random.randint(10, size=100) # 构建了100个整数，取自0到9  
for i in range(100):  
    s = np.random.randint(10) # 先随机选定一个列表的size  
    test_list = [np.random.randint(low=0, high=10, size=s).tolist() for i in range(100)] # 构建了100个列表  
ret = []  
for i in range(100):  # 每个参数都有  
    ret.append(  
        ["函数为format_number("+str(test_num[i])+","+str(test_decimals[i])+","+str(test_list[i])+")="+str(format_number(test_num[i], test_decimals[i], test_list[i]))])  
for i in range(100):  # 缺少第一个参数  
    ret.append(  
        ["函数为format_number("+str(test_num[i])+","+str(test_list[i])+")="+str(format_number(test_num[i], test_decimals[i], test_list[i]))])  
for i in range(100):  # 缺少第二个参数  
    ret.append(  
        ["函数为format_number("+str(test_num[i])+","+str(test_decimals[i])+str(format_number(test_num[i], test_decimals[i], test_list[i]))])  
for i in range(100):  # 两个参数都没有  
    ret.append(  
        ["函数为format_number("+str(test_num[i])+")="+str(format_number(test_num[i], test_decimals[i], test_list[i]))])  
print(ret)
```
**ANS:**
最终的答案是一个二维列表。
```
[['函数为format_number(-1.2177798824606119,6,[5, 1, 6, 3, 9, 0, 7, 0])=-1.217780']...]
```

### Question 2.
**code:**
```python
A = np.array([[1, 0, -3, 0, 5],  
              [4, -1, 3, -2, 9],  
              [0, 3, 2, -5, 1],  
              [0, 0, 1, -4, 7],  
              [9, 8, 7, 6, 5]])  
b = np.array([1, 2, 3, 4, 5])  
x = np.linalg.solve(A, b)  
print(x)
```
**ANS:**
```
[-0.86199095  0.78506787  0.37669683  0.14140271  0.59841629]
```

### Question 3.
**code:**
```matlab
[u,v] = meshgrid(0:pi/100:2*pi);
x = cos(v).*[6-(5/4+sin(3*u))*sin(u-3*v)]
y = sin(v).*[6-(5/4+sin(3*u))*sin(u-3*v)]
z = -cos(u-(3*v))./(5/4+sin(3*u))
surf(x, y, z);
```
**ANS:**
见PDF文件
### Question 4.
**ANS:**
见PDF文件
### Question 5.
**ANS:**

The **Riemann zeta function** or **Euler–Riemann zeta function**, denoted by the Greek letter $\zeta$ (zeta), is a mathematical function of a complex variable $s = \sigma + it$defined as
$$\zeta(s)=\sum_{n=1}^\infty{\frac{1}{n^s}}= \frac{1}{1^s} + \frac{1}{2^s}+\frac{1}{3^s} +\cdots$$
for ${\rm Re}(s) \gt 1$and its analytic continuation elsewhere. When ${\rm Re}(s) = \sigma\gt 1$, the function can be written as a converging summation or integral:
$$\zeta(s)=\sum_{n=1}^\infty{\frac{1}{n^s}}= \frac{1}{\Gamma(s)}\int_{0}^{\infty}\frac{x^{s-1}}{e^x-1}\rm dx$$
where
$${\Gamma(s)} = \int_{0}^{\infty}{x^{s-1}}{e^{-x}}\rm dx$$
is the gamma function. 

In 1737, the connection between the zeta function and prime numbers was discovered by Euler, who proved the identity
$$\sum_{n=1}^\infty{\frac{1}{n^s}} = \prod_{p\ prime}\frac{1}{1-p^{-s}},$$
where, by definition, the left hand side is $\zeta(s)$ and the infinite product on the right hand side extends over all prime numbers (such expressions are called Euler products):
$$\prod_{p\ prime}\frac{1}{1-p^{-s}} = \frac{1}{1-2^{-s}}\cdot\frac{1}{1-3^{-s}}\cdot\frac{1}{1-5^{-s}}\cdot\frac{1}{1-7^{-s}}\cdot\frac{1}{1-11^{-s}}\cdots\frac{1}{1-p^{-s}}\cdots$$
Both sides of the Euler product formula converge for ${\rm Re}(s) \gt 1$.
