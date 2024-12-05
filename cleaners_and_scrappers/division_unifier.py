from pathlib import Path
import os
import re


# Takes the numeric portion of a file and increases by a determined amount
def updated_index(txt):
    str_index = re.sub(r'\D', '', txt)
    index = int(str_index)
    new_index = index + 1
    updated_index = str(new_index)
    return updated_index

folder_paths = []


directory = Path("placeholder/path")

# Update the index of each file on the dietory
for txt in os.listdir("placeholder/path"):
    old_file_name = txt
    index = updated_index()

# Specify the new file name
    new_file_name = f"link_{index}.txt"

# Construct the old and new file paths
    old_file_path = directory / old_file_name
    new_file_path = directory / new_file_name

# Rename the file
    old_file_path.rename(new_file_path)
