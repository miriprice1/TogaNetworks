import os
def single_number(nums):
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    return xor_sum

nums_input = input("Enter space-separated numbers: ")
numbers = [int(num) for num in nums_input.split()]
result = single_number(numbers)
print(f"XOR sum: {result}")
print("hello world")
print("have a good day (:")