from pydub import AudioSegment
from pydub.silence import detect_nonsilent
import os
import subprocess

def convert_adpcm_to_pcm(file_path, output_path):
    """
    Конвертирует adpcm_ima_wav в pcm_wav с использованием ffmpeg.
    """
    command = [
        'ffmpeg',
        '-i', file_path,
        '-acodec', 'pcm_s16le',
        output_path
    ]
    subprocess.run(command)

def remove_sil(path_in, path_out, format="wav"):
    sound = AudioSegment.from_file(path_in, format=format)
    non_sil_times = detect_nonsilent(sound, min_silence_len=50, silence_thresh=sound.dBFS * 1.5)

    if len(non_sil_times) > 0:
        non_sil_times_concat = [non_sil_times[0]]
        
        if len(non_sil_times) > 1:
            for t in non_sil_times[1:]:
                if t[0] - non_sil_times_concat[-1][-1] < 200:
                    non_sil_times_concat[-1][-1] = t[1]
                else:
                    non_sil_times_concat.append(t)
                    
        non_sil_times = [t for t in non_sil_times_concat if t[1] - t[0] > 350]

        # Добавляем 0.05 секунды (50 мс) в начале и 0.3 секунды (300 мс) в конце
        start_time = max(0, non_sil_times[0][0] - 50)
        end_time = non_sil_times[-1][1] + 300

        sound[start_time: end_time].export(path_out, format='wav')

# Запуск функции для всех файлов в директории
directory = input("где файлы?: ")  # Укажите путь к папке с вашими wav-файлами
output_directory = input("куда сохранять?: ") # Путь, где вы хотите сохранить обрезанные файлы

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

for file_name in os.listdir(directory):
    if file_name.endswith('.wav'):
        file_path = os.path.join(directory, file_name)
        converted_path = os.path.join(directory, "converted_" + file_name)
        
        # Конвертация файла
        convert_adpcm_to_pcm(file_path, converted_path)
        
        output_path = os.path.join(output_directory, file_name)
        remove_sil(converted_path, output_path)
        
        # Удаление временного преобразованного файла
        os.remove(converted_path)
