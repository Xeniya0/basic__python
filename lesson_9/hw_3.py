class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = {"wage": wage, "bonus": bonus}

class Position(Worker):

    def get_full_name(self):
        print(f'{self.name} {self.surname}')
    def get_total_income(self):
        print(f'{sum(self._income.values())} денег')

p = Position('Иван', 'Иванов', 'работник', 10, 5)
p.get_full_name()
p.get_total_income()