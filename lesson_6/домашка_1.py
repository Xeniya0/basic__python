with open('nginx_logs.txt', 'r', encoding='utf-8') as f:
    lines_1 = []
    for line in f:
        line = list(line.replace('"', ' ').split(' '))
        lines = (line[0], line[6], line[7])
        lines_1.append(lines)
    print(lines_1)