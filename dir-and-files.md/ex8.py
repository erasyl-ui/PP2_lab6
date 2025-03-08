# Delete a file by specified path after checking access
import os

def delete_file(path):
    if os.path.exists(path):
        if os.access(path, os.W_OK):
            os.remove(path)
            print(f"File '{path}' deleted successfully.")
        else:
            print("No permission to delete the file.")
    else:
        print("File does not exist.")

input("Press Enter to delete a file...")

path = "example.txt"  # Change to your file path
delete_file(path)

# Example:
# If "example.txt" exists and is writable:
# File 'example.txt' deleted successfully.
# If file does not exist:
# File does not exist.
