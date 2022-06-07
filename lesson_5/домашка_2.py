my_num = int(input('number: '))
my_gen = (num for num in range(1, my_num+1) if num % 2 != 0)

print(*my_gen)