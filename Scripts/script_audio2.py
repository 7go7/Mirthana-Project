import os
import whisper

def transcribe_file(file_path):
    model = whisper.load_model("medium").to('cuda')
    result = model.transcribe(file_path, language="Russian")
    return result["text"]

def main():
    folder_path = input("Please enter the path to the audio folder: ")
    output_txt_path = "D:/work/Archolos/transcriptions.txt"

    audio_files = [file for file in os.listdir(folder_path) if file.endswith('.wav')]
    total_files = len(audio_files)

    with open(output_txt_path, 'w') as f:
        for index, file_name in enumerate(audio_files, 1):
            print(f"{index}/{total_files} *{file_name} - working on")
            full_path = os.path.join(folder_path, file_name)
            try:
                transcript = transcribe_file(full_path)
                f.write(f"*{file_name} : \"{transcript}\",""\n")
            except Exception as e:
                print(f"Error transcribing {file_name}: {e}")

    print("All files have been processed!")

if __name__ == "__main__":
    main()
