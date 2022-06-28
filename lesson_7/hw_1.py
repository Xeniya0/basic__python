import os

dir_name = 'my_project'
dir_1, dir_2, dir_3, dir_4 = 'settings', 'mainapp', 'adminapp', 'authapp'
new_path = os.path.join(os.getcwd())

if not dir_name in new_path:
    os.mkdir(dir_name)
    os.chdir(dir_name)
    if not os.path.exists(dir_1 and dir_2 and dir_3 and dir_4):
        os.mkdir(dir_1)
        os.mkdir(dir_2)
        os.mkdir(dir_3)
        os.mkdir(dir_4)