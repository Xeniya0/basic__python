from os import walk, listdir, path
import shutil

dir_name = 'my_project_1'

# for root, dirs, files in walk(dir_name):
#     print(root, dirs, files)

for root, dirs, files in walk(dir_name):
    if 'templates' in dirs and root != dir_name:
        for entry in listdir(path.join(root, 'templates')):
            shutil.copytree(path.join(root, 'templates', entry),
                            path.join(dir_name, 'templace', entry))