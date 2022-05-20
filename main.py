import os
from pprint import pprint

PATH_DIR = 'text'
REZ_FILE_NAME = 'rez.txt'

def file_name(dir_=PATH_DIR):
    pre_full_path = os.path.join(os.getcwd(), dir_)
    file_name = os.listdir(path=pre_full_path)
    return file_name

def get_text_(file):
    dict_text = {}
    for name in file:
        with open(os.path.join(os.getcwd(), PATH_DIR, name), 'r', encoding = 'utf-8') as file:
            lines = [line.strip('') for line in file]
            dict_text[len(lines)] = f'{name}\n{len(lines)}\n{"".join(lines)}'
    dict_text = dict(sorted(dict_text.items()))
    text = dict_text.values()
    return text

with open(os.path.join(os.getcwd(), REZ_FILE_NAME), 'w', encoding='utf-8') as file_:
    file_.write('\n'.join(get_text_(file_name())))
    print(f'Фаил {REZ_FILE_NAME} создан')