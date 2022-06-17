users_hobby = []
users_hobby_1 = {}

with open('users.csv', 'r', encoding='utf-8') as users:
    with open('hobby.csv', 'r', encoding='utf-8') as hobby:
        for user in users:
            users_hobby.append(user.strip())
        for hob in hobby:
            users_hobby.append(hob.strip())

for uh in users_hobby:
    while len(users_hobby) > 1:
        users_hobby_1.setdefault(users_hobby[0], users_hobby[-1])
        users_hobby.pop(0)
        users_hobby.pop(-1)
    if len(users_hobby) == 1:
        users_hobby_1.setdefault(users_hobby[0])
print(users_hobby_1)