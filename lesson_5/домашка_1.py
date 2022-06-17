def my_gen(num):
    for i in range(1, num+1):
        if i % 2 != 0:
            yield i

print(*my_gen(15))