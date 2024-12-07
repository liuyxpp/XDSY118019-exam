import re  

def find_name_value(folder_name):  
    '''Split the name of a data directory into a (name, value) tuple.  

    The format of ``folder_name``:  

        <name><value>  

    If the value is negative, it should be followed by a 'n'.  

    Args:  
        folder_name (str): the name of a :term:`data directory`.  

    Returns:  
        tuple: a tuple contains:  

            * name (str): variable name.  
            * value (float): value of the variable.  
    '''  
    pattern = '([-+]?\d*\.\d+|[-+]?\d+)'  
    rst = re.split(pattern, folder_name)  
    if len(rst) < 2:  
        return folder_name, None  
    name = rst[0]  
    valuestr = rst[1]  
    sign_str = ''  
    if len(rst) > 2:  
        sign_str = rst[2]  
    if sign_str == 'n':  
        value = '-' + valuestr  
    else:  
        value = valuestr  

    return name, float(value)  

# 新增解析多个变量的函数  
def parse_folder_names(folder_name):  
    # 匹配多个变量，支持以下格式的变量提取  
    # regex: 变量名+（正负数值） 可以为小数  
    parts = re.findall(r'([a-zA-Z]+[-+]?\d*\.*\d*n?)', folder_name)  
    results = []  
    for part in parts:  
        if part:  # 确保 part 不为空  
            results.append(find_name_value(part))  
    return results  

# 测试用例  
folder_names = [  
    "phi0.1",            # Test Case 1  
    "xN14.2",            # Test Case 2  
    "kappa0.5n",         # Test Case 3  
    "a1_b14n_n0_c0.2"    # Test Case 4  
]  

# 输出结果  
for folder_name in folder_names:  
    result = parse_folder_names(folder_name)  
    print(f'输入: "{folder_name}" => 输出: {result}')