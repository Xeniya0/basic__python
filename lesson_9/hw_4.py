from random import randint

class Car:
    def __init__(self, n, c, is_Police = False):
        self.name = n
        self.color = c
        self.speed = randint(0, 70)
        self.is_Police = is_Police

    def go(self):
        print(f'машина {self.name} цвета {self.color} поехала со скоростью {self.speed} км/ч, is_Police = {self.is_Police}')
    def stop(self):
        print(f'машина {self.name} цвета {self.color} остановилась, is_Police = {self.is_Police}')
    def turn(self, side):
        print(f'машина {self.name} цвета {self.color} повернула в {side}, is_Police = {self.is_Police}')
    def show_speed(self):
        print(f'машина {self.name} цвета {self.color} движется со скоростью {self.speed} км/ч, is_Police = {self.is_Police}')

class TownCar(Car):
    def show_speed(self):
        super().show_speed()
        if  self.speed > 60:
            print('! превышение скорости !')

class WorkCar(Car):
    def show_speed(self):
        super().show_speed()
        if  self.speed > 40:
            print('! превышение скорости !')

tc = TownCar('Lexus', 'белый')
wc = WorkCar('Police_car',  'белый', is_Police = True)
tc.show_speed()
wc.show_speed()