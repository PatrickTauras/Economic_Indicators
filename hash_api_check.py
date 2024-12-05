import os
import hashlib

def compute_file_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):  # Read in chunks for large files
            hash_object.update(chunk)
    return hash_object.hexdigest()

# Compute hashes for all raw data files
repo_path = "./Raw_Data" #should be run when only the raw datasets are there, if need to run again, add raw data files to their own folder, and change this to the folder's name
hashes = {}
for root, _, files in os.walk(repo_path):
    for file_name in files:
        file_path = os.path.join(root, file_name)
        hashes[file_name] = compute_file_hash(file_path)

# Save hashes to a JSON file
import json
with open("hash_storage/file_hashes.json", "w", encoding="utf-8") as hash_file:
    json.dump(hashes, hash_file, indent=4)

print("Hashes stored in file_hashes.json")
