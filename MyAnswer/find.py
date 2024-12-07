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

# 测试用例  
test_cases = [  
    "phi0.1",        # Test Case 1  
    "xN14.2",        # Test Case 2  
    "kappa0.5n",     # Test Case 3  
    "invalidInput",  # Test Case 4  
    "t1.0",          # Test Case 5  
    "var-2.5",       # Test Case 6  
    "xN0",           # Test Case 7  
    "value.999n",    # Test Case 8  
    "",               # Test Case 9  
    "test-n1.3",     # Test Case 10  
]  

# # 输出结果  
# for test_case in test_cases:  
#     result = find_name_value(test_case)  
#     print(f'输入: "{test_case}" => 输出: {result}')


folder_names = ["phi0.1_xN14.2_kappa0.5n", "a1_b14n_n0_c0.2"]  


for folder_name in folder_names:  
    results = []  
    parts = re.findall(r'([a-zA-Z]+\d*[-+]?\d*\.\d*n?)', folder_name)  
    for part in parts:  
        results.append(find_name_value(part))  
    print(results)
