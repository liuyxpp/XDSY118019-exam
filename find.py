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
        pattern = '([-+]?\d*\.\d+|[-+]?\d+)(n?)$'
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
    legal_input = ["Phi0.1", "xN14.2", "Kappa0.3n", "Kappa0.4n", "Kappa0.5n"]
    illegal_input = ["Phi0.1nn"]
    Boundary_input = ["", "+", ".5", ""]
    input_list = legal_input + illegal_input + Boundary_input
    for name in input_list:
        print(name, find_name_value(folder_name=name))