# List only directories, files, and all directories, files in a specified path
import os

def list_files_dirs(path):
    print("Directories:", [d for d in os.listdir(path) if os.path.isdir(os.path.join(path, d))])
    print("Files:", [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))])
    print("All:", os.listdir(path))

input("Press Enter to list directories and files...")

path = "."  # Change this to any path you want to check
list_files_dirs(path)

# Example:
# If the directory contains "file1.txt", "file2.txt", and "folder1":
# Directories: ['folder1']
# Files: ['file1.txt', 'file2.txt']
# All: ['file1.txt', 'file2.txt', 'folder1']
