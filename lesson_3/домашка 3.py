def thesaurus(*args):
    names = {}
    for x in args:
        key = x[0]
        names.setdefault(key, []).append(x)
    print(names)

thesaurus("Иван", "Мария", "Петр", "Илья")