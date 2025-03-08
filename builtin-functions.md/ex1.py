# Multiply all the numbers in a list
from functools import reduce 

def multiply_list(numbers):
    return reduce(lambda x, y: x * y, numbers)

input("Press Enter to multiply the numbers in the list...")

numbers = [2, 3, 4, 5]  
print("Product of numbers:", multiply_list(numbers))  

# Example:
# numbers = [2, 3, 4, 5]
# Product of numbers: 120
