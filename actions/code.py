"""Some python code"""

import math


def convert_number(num):
    """Converts a number to integer"""
    if isinstance(num, int):
        return num
    if isinstance(num, float):
        return math.floor(num)
    if isinstance(num, str):
        try:
            new_num = int(num)
        except ValueError:
            raise SyntaxError("Provide a number")
    raise SyntaxError("Provide a number")
