# coding: utf-8

import os
import ast

def read_map_from_file(filename):
    """Читает содержимое файла и возвращает словарь"""
    with open(filename, 'r') as file:
        content = file.read()
        # Используем ast.literal_eval для безопасного преобразования строки в словарь
        return ast.literal_eval(content)

def get_new_name(directory, base_name, extension, counter=0):
    """Функция для генерации нового имени файла при дублировании"""
    if counter:
        new_name = f"{base_name} ({counter}).{extension}"
    else:
        new_name = f"{base_name}.{extension}"
    
    if new_name in os.listdir(directory):
        return get_new_name(directory, base_name, extension, counter + 1)
    else:
        return new_name

def rename_files(directory, filename):
    file_map = read_map_from_file(filename)
    for old_name, new_base_name in file_map.items():
        old_path = os.path.join(directory, old_name)
        
        # Проверяем, есть ли расширение у нового имени
        if '.' in new_base_name:
            base, extension = new_base_name.rsplit('.', 1)
        else:
            base = new_base_name
            extension = old_name.rsplit('.', 1)[1] if '.' in old_name else ''
        
        new_name = get_new_name(directory, base, extension)
        new_path = os.path.join(directory, new_name)
        
        if os.path.exists(old_path):
            os.rename(old_path, new_path)
            print(f"rename {old_name} to {new_name}")

# Указываем путь к директории, где находятся файлы и путь к текстовому файлу со словарём
directory_path = r"D:\work\Archolos\MADE\Markus1\mv2\audio"
mapping_file = r"D:\work\Archolos\MADE\Markus1\mv2\rename.txt"
rename_files(directory_path, mapping_file)
