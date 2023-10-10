import tkinter as tk
from tkinter import filedialog
import os
import librosa


def calculate_total_duration(directory):
    total_duration = 0

    for subdir, dirs, files in os.walk(directory):
        for file in files:
            if file.lower().endswith('.wav'):
                filepath = subdir + os.sep + file
                try:
                    total_duration += librosa.get_duration(path=filepath)
                except:
                    print(f"Error reading {filepath}. Skipping...")
                    
    return total_duration

# Tkinter код:
def browse_directory():
    folder_selected = filedialog.askdirectory()
    directory_entry.delete(0, tk.END)
    directory_entry.insert(tk.END, folder_selected)

def display_duration(directory):
    total_seconds = calculate_total_duration(directory)
    hours = total_seconds // 3600
    minutes = (total_seconds % 3600) // 60
    seconds = total_seconds % 60

    duration_label.config(text=f"Total Duration: {int(hours)}h {int(minutes)}m {int(seconds)}s")

root = tk.Tk()
root.title("Audio Duration Calculator")

frame = tk.Frame(root)
frame.pack(padx=20, pady=20)

directory_label = tk.Label(frame, text="Directory:")
directory_label.grid(row=0, column=0, sticky=tk.W, pady=(0, 10))

directory_entry = tk.Entry(frame, width=50)
directory_entry.grid(row=1, column=0, sticky=tk.W, pady=(0, 10))

browse_button = tk.Button(frame, text="Browse", command=browse_directory)
browse_button.grid(row=1, column=1, sticky=tk.W, pady=(0, 10))

calculate_button = tk.Button(frame, text="Calculate Duration", command=lambda: display_duration(directory_entry.get()))
calculate_button.grid(row=2, column=0, columnspan=2, pady=(10, 10))

duration_label = tk.Label(frame, text="")
duration_label.grid(row=3, column=0, columnspan=2, sticky=tk.W)

root.mainloop()
