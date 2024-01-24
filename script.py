# import os
# def single_number(nums):
#     xor_sum = 0
#     for num in nums:
#         xor_sum ^= num
#     return xor_sum

# a = [int(num) for num in os.environ["XOR_NUMBERS"].split()]
# print(single_number(a))
# print("hello world")
# print("have a good day (: ")

# # nums_input = input("Enter space-separated numbers: ")
# # numbers = [int(num) for num in nums_input.split()]
# # result = single_number(numbers)
# # print(f"XOR sum: {result}")
# # print("hello world")
# # print("have a good day (: ")
import sys

def single_number(nums):
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    return xor_sum

# Check if command-line arguments are provided
if len(sys.argv) < 2:
    print("Usage: python script.py <num1> <num2> ...")
    sys.exit(1)

# Extract numbers from command-line arguments
a = [int(arg) for arg in sys.argv[1:]]
print(f"XOR sum: {single_number(a)}")
