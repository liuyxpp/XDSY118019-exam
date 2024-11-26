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
        pattern = '([-+]?\\d*\\.\\d+|[-+]?\\d+)'
        rst = re.split(pattern, folder_name)  
        if len(rst) < 2:  
            return folder_name, None
        name = rst[0]
        valuestr = rst[1]
        sign_str = ''
        if len(rst) > 2 and rst[2] == 'n': 
            if float(rst[1]) < 0:
                sign_str = ''
            else:    
                sign_str = '-'
        value = sign_str + valuestr
        return name, float(value)
def parse_file_name(file_name):
    parts = file_name.split('_')  # 按下划线拆分
    results = []
    for part in parts:
        name, value = find_name_value(part)  # 调用已有函数逐部分解析
        results.append((name, value))
    return results    
print(parse_file_name(file_name = "phi0.1_xN14.2_kappa0.5n"))
print(parse_file_name(file_name = "a1_b14n_n0_c0.2"))