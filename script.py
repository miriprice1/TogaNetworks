import os
def single_number(nums):
    xor_sum = 0
    for num in nums:
        xor_sum ^= num
    return xor_sum

a = [int(num) for num in os.environ["XOR_NUMBERS"].split()]
print(single_number(a))
print("hello world")