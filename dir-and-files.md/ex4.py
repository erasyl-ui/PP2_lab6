# Count the number of lines in a text file
def count_lines(filename):
    with open(filename, 'r') as file:
        return sum(1 for line in file)

input("Press Enter to count lines in a file...")

filename = "example.txt"  # Change to your file name
print("Number of lines:", count_lines(filename))

# Example:
# If "example.txt" has 5 lines:
# Number of lines: 5
