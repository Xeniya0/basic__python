numbers = [57.8, 46.51, 97, 4.06, 22.22, 10]

for number in numbers:
    rub = int(number)
    cop = round((float(number) - int(number))*100)
    if cop < 10:
        print(f'{rub} руб {"0"+str(cop)} коп')
    else:
        print(f'{rub} руб {cop} коп')