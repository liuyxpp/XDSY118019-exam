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
        pattern = r'(\d*\.\d+|\d+)'
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



if __name__ == '__main__':
    # normal inputs
    print(find_name_value('test66'))
    print(find_name_value('phi0.1'))
    print(find_name_value('kappa14.5n'))
    print(find_name_value('xN18n'))
    print()

    # abnormal inputs
    print(find_name_value('31.4'))
    print(find_name_value('hello'))
    print(find_name_value('5.8ABC'))
    print(find_name_value('xN+15'))
    print(find_name_value('hello123hi456.0'))
    print()

    # corner inputs
    print(find_name_value('0'))
    print(find_name_value('n'))
    print(find_name_value('n0'))
    print(find_name_value('0n'))
    print(find_name_value('n0n'))
    print(find_name_value('0n0'))
    print()

    print(find_name_value('-6n'))