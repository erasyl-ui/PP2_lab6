# Generate 26 text files named A.txt to Z.txt
import string

def generate_files():
    for letter in string.ascii_uppercase:
        with open(f"{letter}.txt", 'w') as file:
            file.write(f"This is {letter}.txt")

input("Press Enter to generate 26 text files...")

generate_files()

# Example:
# Files created: A.txt, B.txt, ..., Z.txt
# Each file contains: "This is A.txt", "This is B.txt", etc.
