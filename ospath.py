import os
from datetime import datetime

FOLDER = "DATA"
FILE_NAME = "alice.txt"

file_path = os.path.join(FOLDER, FILE_NAME)
print(f"{file_path = }")

print(f"{os.path.getsize(file_path) = }")
print(f"{os.path.isdir(file_path) = }")
print(f"{os.path.isfile(file_path) = }")
print(f"{os.path.exists(file_path) = }")
print(f"{os.path.dirname(file_path) = }")
print(f"{os.path.basename(file_path) = }")
print(f"{os.path.abspath(file_path) = }")

raw_ts = os.path.getmtime(file_path)
print(f"{raw_ts = }")
file_ts = datetime.fromtimestamp(raw_ts)
print(f"{file_ts = }")
print(f"{os.path.split(file_path) = }")
print(f"{os.path.splitext(file_path) = }")


all_files = os.listdir("SETUP")
print(f"{all_files = }")
