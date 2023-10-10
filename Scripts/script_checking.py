import os

def get_folder_path(prompt):
    while True:
        folder_path = input(prompt)
        if os.path.isdir(folder_path):
            return folder_path
        else:
            print("Invalid path or directory doesn't exist. Please try again.")

def get_tags():
    return input("Enter file tags separated by spaces (e.g., DIA_KURT tria_kurt): ").lower().split()

def check_missing_audio(original_folder, received_folder, tags, missing_output_file, extra_output_file):
    # Получить список всех файлов из оригинальной папки, содержащих указанные теги в названии
    original_files = [f.lower() for f in os.listdir(original_folder) if any(tag in f.lower() for tag in tags)]

    # Получить список всех файлов из папки с присланными аудиофайлами
    received_files = [f.lower() for f in os.listdir(received_folder)]

    missing_files = []
    extra_files = []

    # Проверить, какие файлы отсутствуют в присланной папке
    for file in original_files:
        if file not in received_files and "_15" not in file:
            missing_files.append(file)

    # Проверить, какие файлы лишние в присланной папке
    for file in received_files:
        if file not in original_files:
            extra_files.append(file)

    # Записать отсутствующие файлы в текстовый файл
    with open(missing_output_file, 'w') as f:
        for missing in missing_files:
            f.write(f"{missing} - missing audio\n")

    # Записать лишние файлы в другой текстовый файл
    with open(extra_output_file, 'w') as f:
        for extra in extra_files:
            f.write(f"{extra} - extra audio\n")

if __name__ == "__main__":
    print("Please provide the paths to the folders:")
    original_folder_path = get_folder_path("Enter path to the original folder: ")
    received_folder_path = get_folder_path("Enter path to the received folder: ")

    tags = get_tags()

    output_file_path = "missing_files.txt"
    extra_output_file_path = "extra_files.txt"

    check_missing_audio(original_folder_path, received_folder_path, tags, output_file_path, extra_output_file_path)
