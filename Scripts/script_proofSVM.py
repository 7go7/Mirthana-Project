import os

# Step 1: Read the file and extract all file names
with open("D:\work\Archolos\svm_34(2).txt", 'r',encoding="utf-8") as f:
    lines = f.readlines()

file_names_in_text = {line.split(":")[0].strip('"').lower() for line in lines}

# Step 2: List all files in the directory and extract their base names (without extensions)
folder_path = "D:\work\Archolos\ALL_in_ONE"
files_in_folder = os.listdir(folder_path)

# Store files in lowercase for comparison but keep a mapping to the original case for output
base_names_in_folder = {os.path.splitext(file)[0].lower(): os.path.splitext(file)[0] for file in files_in_folder if "SVM_34" in file.upper()}

# Step 3: Find which files are in the folder but not in the text file
missing_files_in_text = set(base_names_in_folder.keys()) - file_names_in_text

# Step 4: Output this list using the original casing from the folder
with open('missing_in_text.txt', 'w') as output:
    for file_name in sorted(missing_files_in_text):
        output.write(base_names_in_folder[file_name] + '\n')
