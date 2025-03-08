# Test whether a given path exists or not and find the filename and directory
import os

def path_info(path):
    if os.path.exists(path):
        print("Path exists")
        print("Directory:", os.path.dirname(path))
        print("Filename:", os.path.basename(path))
    else:
        print("Path does not exist")

input("Press Enter to check if the path exists...")

path = "example.txt"  # Change this to your desired path
path_info(path)

# Example:
# Path exists
# Directory: /home/user/docs
# Filename: example.txt
