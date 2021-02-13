# this script will get the md5 sum of all files in a folder

# TODO: add logic to check subfolders
# TODO: add logic to alert on a matched MD5

import hashlib
import os

md5_hash = hashlib.md5()

dir_input = input("Directory: ")
filenames = []
md5_hashes = []

for file in os.listdir(dir_input):
    full_path = dir_input + file
    try:
        with open(full_path, 'rb') as file_to_hash:
            filenames.append(file)
            file_content = file_to_hash.read()
            md5_hash.update(file_content)
            md5_hashes.append(md5_hash.hexdigest())
    except PermissionError:
        pass
    except FileNotFoundError:
        print("Ensure there is a '\\' when specifying a directory.")
        break

print("Unable to parse subfolders currently.\n")
print("File Name:\t\tMD5:")

for filename, md5_sum in zip(filenames, md5_hashes):
    print(filename[:10] + '...\t\t' + md5_sum)
