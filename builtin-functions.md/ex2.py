# Count uppercase and lowercase letters in a string
def count_case(s):
    upper_count = sum(1 for char in s if char.isupper())
    lower_count = sum(1 for char in s if char.islower())
    return upper_count, lower_count

input("Press Enter to analyze the case of letters...")

text = "Hello World!"  
upper, lower = count_case(text)
print("Uppercase letters:", upper)
print("Lowercase letters:", lower)

# Example:
# text = "Hello World!"
# Uppercase letters: 2
# Lowercase letters: 8
