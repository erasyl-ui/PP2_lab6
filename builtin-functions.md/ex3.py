# Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]

input("Press Enter to check if a word is a palindrome...")

word = "madam"  
print(f'Is "{word}" a palindrome?', is_palindrome(word))  

# Example:
# word = "madam"
# Is "madam" a palindrome? True

word = "hello"  
print(f'Is "{word}" a palindrome?', is_palindrome(word))  

# Example:
# word = "hello"
# Is "hello" a palindrome? False
