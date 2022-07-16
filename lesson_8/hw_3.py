from functools import *

def type_logger(x):
    @wraps(x)
    def wrapper(*args, **kwargs):
        nums = [num for num in (*args, *kwargs.values())]
        n = [f'{x.__name__}({num}:{type(num)})' for num in nums]
        print(*n, *x(*args,**kwargs), sep = '\n')
    return wrapper

@type_logger
def calc_cube(*x, **y):
    nums = [num for num in (*x, *y.values()) if isinstance(num,int) or isinstance(num, float)]
    return [num ** 3 for num in nums]

a = calc_cube(5, 11, 8.9, 34)