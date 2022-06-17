import os
from pathlib import Path

folder = 'some_data'
new_path = Path.cwd()

def make_stat(folder):
    stat_of_folder = {
                        100: 0,
                        1000: 0,
                        10000: 0,
                        100000: 0
    }

    for file in os.listdir(fr'{new_path}\{folder}'):
        if os.stat(fr'{new_path}\{folder}\{file}').st_size <= 100:
            stat_of_folder[100] += 1
        elif os.stat(fr'{new_path}\{folder}\{file}').st_size <= 1000:
            stat_of_folder[1000] += 1
        elif os.stat(fr'{new_path}\{folder}\{file}').st_size <= 10000:
            stat_of_folder[10000] += 1
        else:
            stat_of_folder[100000] += 1

    return stat_of_folder

print(make_stat(folder))