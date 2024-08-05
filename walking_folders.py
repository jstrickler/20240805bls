import os

START_FOLDER = "."
# START_FOLDER = os.path.abspath(START_FOLDER)

UNWANTED_FOLDERS = ".git", "SETUP"

for folder_path, subfolder_list, filename_list in os.walk(START_FOLDER):
    for unwanted_folder in UNWANTED_FOLDERS:
        if unwanted_folder in subfolder_list:
            subfolder_list.remove(unwanted_folder)
    print(folder_path)
    for filename in filename_list:
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            file_size = os.path.getsize(file_path)
            print(f"    {file_size:10} {filename}")