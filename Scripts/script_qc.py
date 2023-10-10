import re

def normalize_header(header):
    # Removing the .wav ending if it's present
    if header.endswith(".wav"):
        header = header[:-4]
    # Removing unwanted characters and convert to upper case
    return re.sub(r'[^A-Z0-9_]', '', header.upper())

def normalize_content(content):
    # Replace ё with е, remove certain punctuation marks, remove extra spaces, and convert to lowercase
    content_normalized = re.sub(r'[.,;:!?–-—]', ' ', content.replace('ё', 'е')).lower()
    content_normalized = ' '.join(content_normalized.split())
    return content_normalized

def compare_files(file1, file2, output_file):
    # Parsing file 1
    file1_dict = {}
    with open(file1, 'r', encoding='utf-8') as f1:
        for line in f1:
            match = re.match(r'^"(.*?)": "(.*?)"', line)
            if match:
                header, content = match.groups()
                file1_dict[normalize_header(header)] = normalize_content(content)

    # Parsing file 2
    file2_dict = {}
    with open(file2, 'r', encoding='windows-1251') as f2:
        for line in f2:
            match = re.match(r'^\*(.*?\.wav) : "(.*?)"', line)
            if match:
                header, content = match.groups()
                file2_dict[normalize_header(header)] = normalize_content(content)

    # Comparing headers and content
    mismatches = []
    for header, content in file1_dict.items():
        if "_15" in header:
            continue

        if header in file2_dict:
            if content != file2_dict[header]:
                mismatches.append((header, content, file2_dict[header]))
        else:
            mismatches.append((header, content, None))

    for header, content in file2_dict.items():
        if "_15" in header:
            continue

        if header not in file1_dict:
            mismatches.append((header, None, content))


    # Writing mismatches to the output file
    with open(output_file, 'w', encoding='utf-8') as out:
        for header, content1, content2 in mismatches:
            out.write(f'Header: {header}\n')
            
            # If both content1 and content2 are present, it's a mismatch
            if content1 and content2:
                out.write(f'Mismatch:\n')
                out.write(f'File1 Content: {content1}\n')
                out.write(f'File2 Content: {content2}\n')
            else:
                # Otherwise, one of the headers is missing in one of the files
                if content1:
                    out.write(f'Missing in File2: {content1}\n')
                if content2:
                    out.write(f'Missing in File1: {content2}\n')
            
            out.write('-' * 40 + '\n')


# Example usage
compare_files(r"D:\work\Archolos\MADE\Martha.txt", r'D:\work\Archolos\dist\transcriptions.txt', 'output.txt')
