import re

def find_name_value(folder_name):
    '''Split the name of a data directory into a list of (name, value) tuples.

    The format of ``folder_name``:

        <name><value>

    If the value is negative, it should be followed by a 'n'.

    Examples:
        ::

            phi0.1xN14.2kappa0.5n  # should return [('phi', 0.1), ('xN', 14.2), ('kappa', -0.5)]

    Args:
        folder_name (str): the name of a :term:`data directory`.

    Returns:
        list: a list of tuples, each containing:

            * name (str): variable name.
            * value (float): value of the variable.
    '''
    pattern = r'([a-zA-Z]+)(-?\d*\.\d+|-?\d+)(n?)'
    matches = re.findall(pattern, folder_name)
    result = []
    for match in matches:
        name, value_str, sign = match
        value = float(value_str)
        if sign == 'n':
            value = -value
        result.append((name, value))
    return result

if __name__ == '__main__':
    examples = ['phi0.1_xN14.2_kappa0.5n', 'a1_b14n_n0_c0.2']
    for example in examples:
        print(find_name_value(example))