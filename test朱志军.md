import numpy as np

def format_number(num, decimals=0, last_digit=[]):
    '''Format a number to a string suitable for the name of a data directory.
    Args:
        num (float): a float number to be formatted.
        decimals (Optional[int]): Number of decimal places to round to. If decimals is negative, it specifies the number of positions to the left of the decimal point. Default: 0 (round to integer).
        last_digit (Optional[List(int)]): A list of single digits that is allowed for the last digit of the output number. Default: [] (all digits are allowed).
    Returns:
        str: a string represents a float number.
    '''
    decimals = int(decimals)  # ensure it is an integer
    num_rounded = round(num, decimals)
    if decimals > 0:
        format = '{:.' + repr(decimals) + 'f}'
        numstr = format.format(num_rounded)
    else:
        num_rounded = int(num_rounded)
        numstr = '{:d}'.format(num_rounded)

    numstr = list(numstr)  # to ease manipulation
    last = int(numstr[-1])

    if last_digit:
        if last not in last_digit:
            i = np.searchsorted(np.sort(last_digit), last)
            if i == 0:
                left = last_digit[0]
                right = last_digit[1]
            elif i == len(last_digit):
                left = last_digit[-2]
                right = last_digit[-1]
            else:
                left = last_digit[i - 1]
                right = last_digit[i]
            numstr[-1] = repr(left)
            num_left = float(''.join(numstr))
            numstr[-1] = repr(right)
            num_right = float(''.join(numstr))
            if abs(num) - abs(num_left) < abs(num_right) - abs(num):
                numstr[-1] = repr(left)
            else:
                numstr[-1] = repr(right)

    return ''.join(numstr)









第二题
import numpy as np
from scipy import linalg as lg
arr=np.array([[1,0,-3,0,5],[4,-1,3,-2,9],[0,3,2,-5,1],[0,0,1,-4,7],[9,8,7,6,5]])
arrb =np.array([1,2,3,4,5])
print('sol:',lg.solve(arr,arrb))
sol: [-0.86199095  0.78506787  0.37669683  0.14140271  0.59841629]

第三题
u=linspace(0,0.01,2*pi)
v=linspace(0,0.01,2*pi)
[u,v]=meshgrid(u,v)
x=cos(v)*[6 - (5/4 + sin(3*v))*sin(u-3*v)]
y=sin(v)*[6-(5/4+sin(3*v))*sin(u-3*v)]
 z = -cos(u - 3*v)*(5/4+sin(3*v))
surf(x,y,z)
\!\[markdown picture](untitled.jpg/D_drive/)


第四题
Limit[Sum[1/n^2, {n, 1, m}], m -> \[Infinity]]

$Pi^2/6$

Limit[Sum[1/n^4, {n, 1, m}], m -> \[Infinity]]

$Pi^4/90$

Limit[Sum[1/n^6, {n, 1, m}], m -> \[Infinity]]

$\pi^6/945$

Limit[Sum[1/n^8, {n, 1, m}], m -> \[Infinity]]

$\pi^8/9450$

Limit[Sum[1/n^10, {n, 1, m}], m -> \[Infinity]]

$\pi^{10}/93555$

第五题
The Riemann zeta function or Euler-Riemann zeta function,denoted by the Greek letter$\zeta$(zeta),is a mathematical function of a complex variable s = $\sigma$ + it defined as    
$\zeta$(s)=$\sum_{i=1}^{\infty}\frac{1}{n^s}$=$\frac{1}{1^s}$+$\frac{1}{2^s}$+$\frac{1}{3^s}$+$\dots$

for Re(s) > 1 and its analytic continuation elsewhere.When Re(s)=$\sigma$ > 1,the function can be written as a converging or integral:

$\zeta$(s)=$\sum_{i=1}^{\infty}\frac{1}{n^s}$=$\frac{1}{\Gamma (s)}\int_{0}^{\infty }\frac{x^{s-1}}{e^x-1}dx$
where

${\Gamma (s)}$=$\int_{0}^{\infty }x^{s-1}e^{-x}dx$
is the gamma function.
In 1737, the connection between the zeta function and prime numbers was discovered by Euler, who proved the identity

$\sum_{n=1}^{\infty}\frac{1}{n^s}$=$\prod_{p \text { prime }} \frac{1}{1-p^{-s}}$


where, by definition, the left hand side is $\zeta(s)$ and the infinite product on the right hand side extends over all prime numbers $p$ (such expressions are called Euler products):

$\prod_{p \text { prime }} \frac{1}{1-p^{-s}}=\frac{1}{1-2^{-s}} \cdot \frac{1}{1-3^{-s}} \cdot \frac{1}{1-5^{-s}} \cdot \frac{1}{1-7^{-s}} \cdot \frac{1}{1-11^{-s}} \cdots \frac{1}{1-p^{-s}} \cdots$

Both sides of the Euler product formula converge for $Re(s) > 1$.