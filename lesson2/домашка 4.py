list = ['инженер-конструктор Игорь', 'главный бухгалтер МАРИНА', 'токарь высшего разряда нИКОЛАй', 'директор аэлита']

list_1 = list[0].split()
list_2 = list[1].split()
list_3 = list[2].split()
list_4 = list[3].split()

print('Привет, ', (list_1[-1]).title(), '!', sep='')
print('Привет, ', (list_2[-1]).title(), '!', sep='')
print('Привет, ', (list_3[-1]).title(), '!', sep='')
print('Привет, ', (list_4[-1]).title(), '!', sep='')