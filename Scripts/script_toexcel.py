import os
import re

# Путь к файлу с текстом и папке со звуками
path_to_text_file = r"C:\Users\Андр\Downloads\svm3.txt"
path_to_sound_folder = r'D:\work\Archolos\ALL_in_ONE'

# Путь к файлу, в который будет записываться результат
path_to_output_file = 'svm_1.txt'

# Чтение файла
with open(path_to_text_file, 'r', encoding='utf-8') as file:
    lines = file.readlines()

voiceID = '1'

# Словарь соответствия для замены
replacement_dict = {
    'Common': voiceID,
    'MaleVariant1': voiceID,
    'MaleVariant2': voiceID,
    'MaleVariant3': voiceID,
    'MaleVariant4': voiceID,
    'FemaleVariant1': voiceID,
    'FemaleVariant2': voiceID,
    'FemaleVariant3': voiceID,
    'FemaleVariant4': voiceID,
    '16': voiceID
}

# Паттерн для поиска имен
pattern = r'"(SVM_(Common|16|MaleVariant\d+)_[\w\d]+)":'

# Проверяем каждую строку
with open(path_to_output_file, 'w', encoding='utf-8') as output:
    for line in lines:
        match = re.search(pattern, line)
        if match:
            original_name = match.group(1)
            # Заменяем имя на формат с 19
            new_name = original_name
            for key, value in replacement_dict.items():
                if key in original_name:
                    new_name = original_name.replace(key, value)
                    break
            wav_file_path = os.path.join(path_to_sound_folder, f"{new_name}.wav")
            if os.path.exists(wav_file_path):
                # Заменяем имя в строке и записываем ее в новый файл
                line = line.replace(original_name, new_name)
                output.write(line)

print("done!")
