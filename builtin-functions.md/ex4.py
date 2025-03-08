# Square root function after specific milliseconds
import time
import math

def delayed_sqrt(number, delay):
    time.sleep(delay / 1000)  # Convert milliseconds to seconds
    return math.sqrt(number)

num = 25100
delay_ms = 2123

input(f"Press Enter to find the square root of {num} after {delay_ms} milliseconds...")
result = delayed_sqrt(num, delay_ms)
print(f"Square root of {num} after {delay_ms} milliseconds is {result}")

# Example:
# num = 25100
# delay_ms = 2123
# Square root of 25100 after 2123 milliseconds is 158.42979517754858
