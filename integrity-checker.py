import os
import hashlib

def calculate_sha256(file_path):
    sha256_hash = hashlib.sha256()
    with open(file_path,"rb") as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256_hash.update(data)
    return sha256_hash.hexdigest()

def check_integrity(directory_path):
    if not os.path.esists(directory_path) or not os.path.isdir(directory_path):
        print(f"Directory '{directory_path}' doesn't exist.")
        return
    for root, dirs, files in os.walk(directory_path):
        for file_name in files:
            file_path = os.path.join(root, file_name)
            calculated_hash = calculate_sha256(file_path)
            print(f"File: {file_path} \n SHA-256 Hash: {calculate_sha256}")

if __name__ == "__main__":
    directory_to_check = input("Enter the directory path to check the integrity: ")
    check_integrity(directory_to_check)