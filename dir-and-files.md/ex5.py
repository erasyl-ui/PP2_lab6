# Write a list to a file
def write_list_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(item + "\n")

input("Press Enter to write a list to a file...")

data = ["Apple", "Banana", "Cherry"]
filename = "fruits.txt"
write_list_to_file(filename, data)

# Example:
# The file "fruits.txt" will contain:
# Apple
# Banana
# Cherry
