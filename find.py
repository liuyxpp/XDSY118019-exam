import re

def find_name_value(folder_name):
        '''Split the name of a data directory into a (name, value) tuple.

        The format of ``folder_name``:

            <name><value>

        If the value is negative, it should be followed by a 'n'.

        Examples:
            ::

                phi0.1          # should return 'phi', 0.1
                xN14.2          # should return 'xN', 14.2
                kappa0.5n       # should return 'kappa', -0.5

        Args:
            folder_name (str): the name of a :term:`data directory`.

        Returns:
            tuple: a tuple contains:

                * name (str): variable name.
                * value (float): value of the variable.
        '''
        pattern = '([-+]?\d*\.\d+|[-+]?\d+)'
        parts = folder_name.split('_')
        result = []

        for part in parts:
            rst = re.split(pattern, part)
            if len(rst) < 2:
                result.append((part, None))
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

            result.append((name, float(value)))

        return result

def test_find_name_value():
    # 正常输入
    assert find_name_value('phi0.1') == [('phi', 0.1)]
    assert find_name_value('xN14.2') == [('xN', 14.2)]
    assert find_name_value('kappa0.5n') == [('kappa', -0.5)]
    assert find_name_value('alpha-3.14') == [('alpha', -3.14)]
    assert find_name_value('beta+2.71') == [('beta', 2.71)]
    assert find_name_value('phi0.1_xN14.2_kappa0.5n') == [('phi', 0.1), ('xN', 14.2), ('kappa', -0.5)]

    # 异常输入
    assert find_name_value('gamma') == [('gamma', None)]  # 没有数值部分
    assert find_name_value('deltaNaN') == [('deltaNaN', None)]  # 数值部分不是有效数字
    assert find_name_value('') == [('', None)]  # 空字符串

    # 边界输入
    assert find_name_value('epsilon0') == [('epsilon', 0.0)]  # 数值为 0
    assert find_name_value('zeta-0.0') == [('zeta', -0.0)]  # 数值为 -0.0
    assert find_name_value('eta1234567890') == [('eta', 1234567890.0)]  # 大数值

# 调用测试函数
test_find_name_value()

# 直接调用并打印结果
result1 = find_name_value("phi0.1_xN14.2_kappa0.5n")
result2 = find_name_value("a1_b14n_n0_c0.2")
print(result1)  # 应该输出 [('phi', 0.1), ('xN', 14.2), ('kappa', -0.5)]
print(result2)  # 应该输出 [('a', 1.0), ('b', -14.0), ('n', 0.0), ('c', 0.2)]
