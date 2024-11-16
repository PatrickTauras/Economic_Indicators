import json
import hashlib


def compute_file_hash(file_path):
    hash_object = hashlib.sha256()
    with open(file_path, 'rb') as f:
        while chunk := f.read(8192):  # Read in chunks for large files
            hash_object.update(chunk)
    return hash_object.hexdigest()


#Inflation
file_path = "Inflation_data.json"

hash_value = compute_file_hash(file_path)
print(f"Inflation Hash Value: {hash_value}")

#GDP
file_path = "GDP_data.json"

hash_value = compute_file_hash(file_path)
print(f"GDP Hash Value: {hash_value}")

#Employment
file_path = "Employment_data.json"

hash_value = compute_file_hash(file_path)
print(f"Employment Hash Value: {hash_value}")

#Verification comparing hashes to original values
def verify_json_file(file_path, reference_hash):
    calculated_hash = compute_file_hash(file_path)
    return calculated_hash == reference_hash

# Reference hash from initially calculated hashes in file_hashes.json
employment_reference_hash = "e111f05b9756e476caeaaefa97f93fa7cd6e8ce0243d780d6fe57dbbe65d8297"
GDP_reference_hash = "0e826de848c7a687dc146b30d8dd38a2fef69a941c162bbff013b106e9a6c0cc"
Inflation_reference_hash = "94b18ba159a0d3a9ca5722db931dba279e983394c179e5f80bfd1aa81143776e"

# Verification
is_valid = verify_json_file("Inflation_data.json", Inflation_reference_hash)
print("Inflation Integrity Check Passed" if is_valid else "Inflation Integrity Check Failed")

is_valid = verify_json_file("GDP_data.json", GDP_reference_hash)
print("GDP Integrity Check Passed" if is_valid else "GDP Integrity Check Failed")

is_valid = verify_json_file("Employment_data.json", employment_reference_hash)
print("Employment Integrity Check Passed" if is_valid else "Employment Integrity Check Failed")

