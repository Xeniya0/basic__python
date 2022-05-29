def num_translate():
    num = int(input('введите число: '))
    if num < 11:
        if num == 1:
            print('1 = "one" / "один"')
        elif num == 2:
            print('2 = "two"/"два"')
        elif num == 3:
            print('3 = "three"/"три"')
        elif num == 4:
            print('4 = "four"/"четыре"')
        elif num == 5:
            print('5 = "five"/"пять"')
        elif num == 6:
            print('6 = "six"/"шесть"')
        elif num == 7:
            print('7 = "seven"/"семь"')
        elif num == 8:
            print('8 = "eight"/"врсемь"')
        elif num == 9:
            print('9 = "nine"/"девять"')
        elif num == 10:
            print('10 = "ten"/"десять"')
    else:
        print(None)

num_translate()