import os
import time


directory = r'C:\Users\Maria\Desktop\urban\7 модуль'


for dirpath, dirnames, filenames in os.walk(directory):
    for filename in filenames:

        full_path = os.path.join(dirpath, filename)
        mtime = os.path.getmtime(full_path)
        last_modified_time = time.ctime(mtime)
        file_size = os.path.getsize(full_path)
        parent_directory = os.path.dirname(full_path)

        print(f"Файл: {full_path}")
        print(f"Последнее изменение: {last_modified_time}")
        print(f"Размер: {file_size} байт")
        print(f"Родительская директория: {parent_directory}")
        print("-" * 40)
