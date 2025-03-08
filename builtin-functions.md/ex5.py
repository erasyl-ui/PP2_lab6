# Check if all elements in a tuple are True
def all_true(t):
    return all(t)

input("Press Enter to check if all elements in the tuple are True...")

t = (True, True, True)  
print("All elements in tuple are True:", all_true(t))  

# Example:
# t = (True, True, True)
# All elements in tuple are True: True

t = (True, False, True)  
print("All elements in tuple are True:", all_true(t))  

# Example:
# t = (True, False, True)
# All elements in tuple are True: False
