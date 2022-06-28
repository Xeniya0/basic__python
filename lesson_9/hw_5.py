class Stationery:
    def __init__(self, title = 'изображения'):
        self.title = title

    def draw(self):
        print(f'Запуск отрисовки {self.title}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} ручкой')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} карандашом')

class Handle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки {self.title} маркером')

stationery = Stationery()

pen = Pen('изображения')
pencil = Pencil('рисунка')
handle = Handle('изображения')

my_list = [pen, pencil, handle]

for i in my_list:
    i.draw()