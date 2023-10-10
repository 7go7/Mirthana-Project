import os
import assemblyai as aai

def transcribe_file(file_path, api_key):
    aai.settings.api_key = api_key

    config = aai.TranscriptionConfig(language_code="ru")
    transcriber = aai.Transcriber(config=config)
    transcript = transcriber.transcribe(file_path)

    return transcript.text

def main():
    folder_path = input("Please enter the path to the audio folder: ")
    output_txt_path = "transcriptions.txt"
    api_token = input("Please enter the token (666f244599ca4480a31558f6107a9e71): ")

    audio_files = [file for file in os.listdir(folder_path) if file.endswith('.wav')]
    total_files = len(audio_files)

    with open(output_txt_path, 'w') as f:
        for index, file_name in enumerate(audio_files, 1):
            print(f"{index}\\{total_files} *{file_name} - working on")
            full_path = os.path.join(folder_path, file_name)
            transcript = transcribe_file(full_path, api_token)
            f.write(f"*{file_name} : \"{transcript}\"\n")

    print("All files have been processed!")

if __name__ == "__main__":
    main()
