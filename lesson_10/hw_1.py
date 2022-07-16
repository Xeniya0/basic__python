from abc import  abstractmethod

my_list_1 = [[31, 22], [37, 43], [51, 86]]
my_list_2 = [[3, 5, 32], [2, 4, 6], [-1, 64, -8]]
my_list_3 = [[3, 5, 8, 3], [8, 3, 7, 1]]

class Matrix:
    def __init__(self, list):
        self.list = list

    def __add__(self, other):
        add = Matrix(self.list + other.list)
        add = str(add).replace('], [', '\n').replace('[[', '').replace(']]', '')
        return add

    def __str__(self):
        return f'{self.list}'

a = Matrix(my_list_1)
b = Matrix(my_list_2)
print(a + b)

a = Matrix(my_list_1)
b = Matrix(my_list_3)
print(a + b)

a = Matrix(my_list_2)
b = Matrix(my_list_3)
print(a + b)