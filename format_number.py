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