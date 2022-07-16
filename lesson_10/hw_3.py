class Cell:
    def __init__(self, nums):
        self.nums = nums

    def make_order(self, rows):
        return '\n'.join(['(._.)' * rows for _ in range(self.nums // rows)]) +'\n' + '(._.)' * (self.nums % rows)

    def __str__(self):
        return f'{self.nums}'

    def __add__(self, other):
        print('summ:')
        return Cell(self.nums + other.nums)

    def __sub__(self, other):
        return Cell(self.nums - other.nums) if self.nums - other.nums > 0 \
            else 'No'

    def __mul__(self, other):
        return Cell(self.nums * other.nums)

    def __floordiv__(self, other):
        return Cell(self.nums // other.nums)

ceil_1 = Cell(15)
ceil_2 = Cell(24)
print(ceil_1 + ceil_2)
print(ceil_1 - ceil_2)
print(ceil_1 * ceil_2)
print(ceil_1 // ceil_2)
print(ceil_2.make_order(7))
