# Check for access to a specified path
import os

def check_access(path):
    print("Path exists:", os.path.exists(path))
    print("Readable:", os.access(path, os.R_OK))
    print("Writable:", os.access(path, os.W_OK))
    print("Executable:", os.access(path, os.X_OK))

input("Press Enter to check access permissions...")

path = "example.txt"  # Change this to the path you want to check
check_access(path)

# Example:
# Path exists: True
# Readable: True
# Writable: False
# Executable: False
