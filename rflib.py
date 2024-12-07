"""
This is the unified lib for Root Finding, developed by huanghaiyang

Method provided: Bisection, Newton
Applicable function type : scalar
"""

from sys import float_info
import warnings
# For the change from warning to error to catch it (overflow)

class Root:
    """
    This is a simple class to store the calls, status of convergence, error, the numerical root and the possible alarm during solving.
    """
    def __init__(self, method : str = None, converged : bool = None,
                 iterations : int = None, root : float = None,
                 error : float = None, alarm : list = [],
                 process : list = [], *arg, **kwarg) -> None:
        # for initialize an instance
        self.method = method
        self.iterations = iterations
        self.converged = converged
        self.root = root
        self.error = error
        self.alarm = alarm
        self.process = process
    
    def __str__(self) -> str:
        # for formatting the alarming information and display the `Root`
        alarm = ""
        l = len(self.alarm)
        if l == 0:
            alarm = 'None'
        else:
            alarm = self.alarm[0]
            for i in range(1, l):
                alarm += "\n              " + self.alarm[i]

        return f"\n\
     method : {self.method}\n\
  converged : {self.converged}\n\
iterracions : {self.iterations}\n\
       root : {self.root}\n\
      error : {self.error}\n\
      alarm : {alarm}"

    def show_process(self, show = True):
        # for showing the process of solving 
        # function provided in ver 1.1
        """
        ploting the process of iteration.

        Parameters
        ----------
        show : bool, optional
            determine whether to execute the sentence `plt.show()`, which makes multi-plot being possible
        """
        import matplotlib.pyplot as plt

        process = self.process
        l = len(process)
        x = [i for i in range(l)]

        if self.method == 'Bisection':
            y_a = [process[i][0] for i in range(l)]
            y_b = [process[i][1] for i in range(l)]
            plt.plot(x, y_a, '-o', label = 'Left endpoint')
            plt.plot(x, y_b, '-o', label = 'Right endpoint')
        elif self.method == 'Newton':
            y = [process[i] for i in range(l)]
            plt.plot(x, y, '-o', label = 'Newton method')
        else :
            print("No method used!\n")
            return
        
        plt.xlabel('Iteration times')
        plt.ylabel('Approximate root')
        plt.title('Iteration process')
        plt.legend()

        # Abandoned those codes to draw the numerical root
        '''if self.converged:
            plt.plot([0, l - 1], [self.root, self.root])
            plt.text()'''
        
        try:
            # For those matplotlib with low version, plt.tick_params() isn't available to use the parameter of `direction`, so we use the more common way
            plt.tick_params(axis = 'both', direction = 'in')
        except NameError:
            raise NameError("The version of matplotlib might be too low, please update it!")
        
        if show:
            plt.show()
        return 

def __raise_alarm(alarm : list = [], Error : str = '') -> str:
    temp_alarm = ""
    for str in alarm:
        temp_alarm += str + '\n'
    raise ValueError(temp_alarm + Error)

def __Bisection(f, a = 0, b = 0, epsilon = 100 * float_info.epsilon,
                 alarm : list = []) -> Root:
    """
    Finding the root using the method of Bisection

    Parameters
    ----------
    f : callable
        must be a scalar funtion to find root of, or there will raise error when calling

    a : float
        the left endpoint of the interval to find root on

    b : float
        the right endpoint of the interval to find root on

    epsilon : float, optional
        the shreshold value or the tolerance of the root, default value is 10 times the sys.float_info.epsilon

    alarm : str, optional
        the alarm passed by the father function to show in the final result
    
    Returns
    -------
    Return the informations inlcuding the convergence, calls of function, error, and the numertical root
    Notice that the approximate root is the average of the last pair of (a, b),
    which indicate that the error = (b - a) / 2 < epsilon
    """

    __sgn = lambda x : 1 if x > 0 else (-1 if x < 0 else 0)
    # use the function `sgn` to skip the operation of mutipling two complex number

    epsilon = max(epsilon / 10, float_info.epsilon)
    # the precision is epsilon means that the last position should be exact.
    # we use the stategy of being more precise to avoid the question.
    if a > b :
        __raise_alarm(alarm, "Insensible interval")
    a_sgn = __sgn(f(a))
    b_sgn = __sgn(f(b))
    iterations = 0
    mid = 0
    temp = 0
    dic = [[a, b]]
    # difine them out of the loop, saving time to create them
    if a_sgn == b_sgn and a_sgn != 0:
        mid = (a + b) / 2
        temp = __sgn(f(mid))
        iterations = 1
        if temp == a_sgn:
            __raise_alarm(alarm, "The values of the function at the endpoints of the bracket aren't of opposite signs! Attempting Failed!")
        else:
            # Attempting to correct the interval with the same sign at the endpoint. Only once!
            b = mid
            b_sgn = __sgn(f(b))
            alarm.append("Given endpoints with same sign! Correcting attempt successed!")
            dic.append([a, b])

    if a_sgn == 0:
        return Root('Bisection', True, iterations, a, 0, alarm = alarm, dic = [a, a])
    elif b_sgn == 0:
        return Root('Bisection', True, iterations, b, 0, alarm = alarm, dic = [b, b])
    
    while (b - a > 2 * epsilon):
        mid = (a + b) / 2
        temp = __sgn(f(mid))
        iterations += 1
        if temp == 0:
            a = mid
            b = mid
            dic.append([a, b])
            break
        elif temp * a_sgn < 0:
            b = mid
        else:
            a = mid
        dic.append([a, b])

    return Root('Bisection', True, iterations, (a + b) / 2, (b - a) / 2, alarm = alarm, process = dic)

def __Newton(f, fprime, x0 = None, epsilon = 100 * float_info.epsilon,
              loop_tol = 1000, alarm : list = []) -> Root:
    """
    Finding the root using the method of Bisection

    Parameters
    ----------
    f : callable
        must be a scalar funtion to find root of, or there will raise error when calling

    fprime : callable
        the derivative of f

    x0 : float
        the initial value to start from

    epsilon : float, optional
        the shreshold value or the tolerance of the root, default value is 10 times the sys.float_info.epsilon

    loop_tol : int, optional
        the tolerance of the numbers of loop when iterating, default as 1000 times
    
    alarm : str, optional
        the alarm passed by the father function to show in the final result
    
    Returns
    -------
    Return the informations inlcuding the convergence, calls of function, error, and the numertical root
    Notice that the approximate root is the average of the last pair of (a, b),
    which indicate that the error = (b - a) / 2 < epsilon
    """
    
    abs = lambda x : -x if x < 0 else x
    # if x is quite close to the sys.float_info.epsilon, then 0 comes to -0, which isn't what we are supposed to see.

    if x0 == None:
        alarm.append("No initial value given! Set as 0!")
        x0 = 0
    if not fprime:
        raise ValueError("No derivative given when solving with Newton method!")
    
    epsilon = max(epsilon / 10, float_info.epsilon)
    # the precision is epsilon means that the last position should be exact.
    # we use the stategy of being more precise to avoid the question.
    iterate_calls = 1
    x1 = None
    temp = f(x0)
    dic = []

    warnings.filterwarnings('error', category=RuntimeWarning)
    # Change the warning message `RunTimeWarning` into error message, in order to catch it in the try-except structure

    def __get_x1(x0, f_x0, f_primex0):
        # for the multiple errors or warnings which may encounter during solving, 
        # and for the frequent use or the calling, we develop the function
        if f_primex0 == 0:
            # adding a epsilon to prevent the ZeroDivisionError
            if "Derivative of f equals zero when iterating! Add epsilon!" not in alarm:
                alarm.append("Derivative of f equals zero when iterating! Add epsilon!")
            f_primex0 += float_info.epsilon
        try:
            x1 = x0 - f_x0 / f_primex0
        except RuntimeWarning as run_time_warning:
            alarm.append(f"run time warning : {run_time_warning}")
            return 'error'
        return x1

    if temp == 0:
        x1 = x0
        dic = [x0, x1]
        # There we also return the process with x1, to prevent IndexError
    else:
        temp_prime = fprime(x0)
        x1 = __get_x1(x0, temp, temp_prime)
        if x1 == 'error':
            return Root('Newton', False, iterations = iterate_calls, root = x0, error = 'None', alarm = alarm, process = dic)
        dic = [x0, x1]
    # We choose to store the points that we've been to, 
    # for the O(n^2) time complexity is sometimes less important compared to some function and the derivative of f that are much more complex to calculate
    while(abs(x0 - x1) > epsilon):
        x0 = x1
        temp = f(x0)
        iterate_calls += 1
        if temp == 0:
            x1 = x0
            return Root('Newton', True, iterations = iterate_calls, root = x1, error = 0, alarm = alarm, process = dic)
        else:
            temp_prime = fprime(x0)
            x1 = __get_x1(x0, temp, temp_prime)
            if x1 == 'error':
                return Root('Newton', False, iterations = iterate_calls, root = x0, error = 'None', alarm = alarm, process = dic)
            
            # To check if there exist a cycle during solving
            for i in range(iterate_calls - 1):# dic[iterate_calls - 1] = x0
                if abs(dic[i] - x1) <= float_info.epsilon:
                    alarm.append("Cycle exists during solving!")
                    return Root('Newton', False, iterations = iterate_calls, root = 'None', error = 'None', alarm = alarm, process = 'None')
                
        dic.append(x1)
        if iterate_calls > loop_tol :
            alarm.append("Didn't converge under the limit of numbers of iteration!")
            alarm.append("The root is the latest approximate root while iterating!")
            return Root('Newton', False, iterations = iterate_calls, root = x1, error = 'None', alarm = alarm, process = dic)
    
    temp_error = abs(dic[iterate_calls] - dic[iterate_calls - 1]) / 2
    if temp_error == 0:
        # if the x1 is the exact root, then it will be returned in the former code.
        # this condition means that the error is lower than sys.float_info.epsilon, which makes it to be o
        temp_error = float_info.epsilon
    return Root('Newton', True, iterations = iterate_calls, root = dic[iterate_calls], 
                error = abs(dic[iterate_calls] - dic[iterate_calls - 1]) / 2, alarm = alarm, process = dic)

def root_finding(f, method :str = None, braket : list = None,
                  fprime = None, x0 = None, x1 = None, 
                  epsilon = 100 * float_info.epsilon, loop_tol = 1000,
                  plot = False, plot_interval = None) -> Root:
    """
    Finding a root of a given scalar function

    Parameters
    ----------
    f : callable
        must be a scalar funtion to find root of, or there will raise ValueError

    method : str, optional
        there is two given method to choose from:
            - Bisection : `bracket` needed, which implies the signum of the endpoints funtion value should be opposite
            - Newton :  `fprime`,`x0` needed; `x1` optional.

    bracket : list of two element, optional
        standing for the begining and the end of a interval(endpoints included)

    fprime : callable, optional
        the derivative of f

    x0 : float, optional
        the default start value to try in the method of `Newton`

    x1 : float, optional
        the second start value to try in the method of `Newton`

    epsilon : float, optional
        the shreshold value or the tolerance of the root, default value is 100 times the sys.float_info.epsilon

    loop_tol : int, optional
        the tolerance of the numbers of the loops while using the `Newton` method

    plot : bool, optinal
        whether to plot the objective function

    plot_interval : list, optional
        the interval to plot on, default as bracket, if given, or [-5, 5]
    """

    if plot:
        if plot_interval == None:
            if braket:
                plot_interval = braket
            else:
                plot_interval = [-5, 5]
            print(f"Ploting interval no given, set as {plot_interval}!\n")
        if plot_interval[0] > plot_interval[1]:
            __raise_alarm([], 'Illegal ploting interval!')

        import matplotlib.pyplot as plt
        import numpy as np

        # abandon the following code to suit the demand to show the figure of f and the process in the same plot,
        # for the uncertainty of the calling of `show_process()`
        '''fig_num = len(plt.get_fignums())
        plt.figure(fig_num + 1)
        # for one may display the figure of f and the solving process at the same time, or other immentioned exceptions
        x = np.arange(plot_interval[0], plot_interval[1] + 0.01, 0.01)

        _, ax = plt.subplots()
        # Create the sub plot to move the position of the x-axis to the zero point
        ax.plot(x, f(x))
        ax.spines['bottom'].set_position('zero') '''

        x = np.arange(plot_interval[0], plot_interval[1] + 0.01, 0.01)
        plt.plot(x, f(x), label = 'y=f(x)')
        plt.plot([plot_interval[0], plot_interval[1]], [0, 0], label = 'y=0')
        plt.xlabel('x')
        plt.ylabel('y', rotation = 0)
        plt.title('Figure of f(x)')
        plt.legend()
        plt.show()

    alarm = []
    if method == None:
        if braket:
            method = 'Bisection'
            alarm.append("No method given, automatically chosed as Bisection!")
        elif fprime:
            method = 'Newton'
            alarm.append("No method given, automatically chosed as Newton!")

    if method == 'Bisection':
        return __Bisection(f, braket[0], braket[1], epsilon = epsilon, alarm = alarm)
    
    elif method == 'Newton':
        root = __Newton(f, fprime, x0, epsilon = epsilon, alarm = alarm, loop_tol = loop_tol)
        if x1 and root.converged == False:
            alarm.append(f"First attemption of x_0 = {x0} failed!")
            alarm.append(f"Here comes the second try with the initial value as {x1}")
            root = __Newton(f, fprime, x1, epsilon = epsilon, alarm = alarm, loop_tol = loop_tol)
        return root
    
    else:
        return Root(alarm=["Illegal operation!"])

if __name__ == "__main__":
    '''import numpy as np
    import matplotlib.pyplot as plt
    def f(x):
        return np.tan(x) - 2 * x

    def fprime(x):
        return 1 / (np.cos(x) ** 2) - 1

    #root = root_finding(f, "Newton", fprime = fprime, x0 = 5 * np.pi / 4, x1 = 4.5, plot=True, plot_interval=[np.pi, 2 * np.pi])
    root = root_finding(f, "Bisection", braket=[-0.2, 1.4], plot=False)
    #print(root)
    root.show_process()
    plt.show()'''
    import rflib
    import numpy as np

    def f(x):
        return np.tan(x) - x

    root = rflib.root_finding(f, "Bisection", [np.pi, 2 * np.pi], plot=True)
    print(root)
    root.show_process()