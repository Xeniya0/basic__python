list = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
a = ''

for i in list:
    x = i[-1]
    if x.isdigit():
        if int(i) < 10:
            i = str(f'"{i.replace(x, "0"+x)}"')
    a += i + ' '

print(a)