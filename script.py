import os
import sys

def single_number(nums):
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    return xor_sum

# Check if the environment variable XOR_NUMBERS is set
if "XOR_NUMBERS" not in os.environ:
    print("Error: XOR_NUMBERS environment variable is not set.")
    sys.exit(1)

# Extract numbers from the environment variable
numbers = [int(num) for num in os.environ["XOR_NUMBERS"].split()]
result = single_number(numbers)

print(f"XOR sum: {result}")
