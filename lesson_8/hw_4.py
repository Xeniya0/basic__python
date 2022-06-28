from functools import *

def val_checker(func):
    def val_checker_1(func_1):
        @wraps(func_1)
        def wrapper(num):
            if func(num):
                print(func(num))
            else:
                raise ValueError(f'wrong val {num}')
        return wrapper
    return val_checker_1

@val_checker(lambda x: x> 0)
def calc_cube(x):
    return x ** 3

try:
    a = calc_cube(5)
except(ValueError, TypeError) as err:
    print(err)
