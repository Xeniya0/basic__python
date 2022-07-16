from re import *

def email_parse(email):
    email_adress = email
    username = compile(r'^(\w)\w*')
    domain = compile(r'@\w+\.\w+$')
    parse = {'username' : None, 'domain' : None}
    parse['username'] = str(username.search(email_adress)).strip('>').split('=')[-1]
    parse['domain'] = str(domain.search(email_adress)).strip('>').split('=')[-1]
    if 'None' not in parse.values():
        print(parse)
    else:
        print('wrong email')

email_parse('someone@geekbrains.ru')
email_parse('someone@geekbrainsru')