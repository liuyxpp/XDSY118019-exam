import re
def find_name_value_plus(folder_name):
    pattern = r'^([a-zA-Z]+)([-+]?\d*\.?\d+)(n?)$'
    result = []
    #设置新的正则表达式
    matches = re.findall(pattern, folder_name)
    if not matches:
        raise ValueError("not match with expected format")
    #主动报错:不符合我们需要的格式
    for match in matches:
        name = match[0]
        if match[2] =='n':
            value = -float(match[1])
        else:
            value = float(match[1])
        result.append((name,value))
    return result

print(find_name_value_plus(input("input:")))


