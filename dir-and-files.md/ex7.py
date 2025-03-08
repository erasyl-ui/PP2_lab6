# Copy the contents of a file to another file
def copy_file(source, destination):
    with open(source, 'r') as src, open(destination, 'w') as dest:
        dest.write(src.read())

input("Press Enter to copy file contents...")

source = "source.txt"  # Change to your file
destination = "destination.txt"
copy_file(source, destination)

# Example:
# If "source.txt" contains "Hello, World!", "destination.txt" will also contain "Hello, World!"
