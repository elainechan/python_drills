"""
flipping_bits.py

You're given a list of positive integers. 
Convert each number in turn to a 32-bit, unsigned binary numbers.
Flip the bits, and print the new decimal number.

Example:
Input: 1
As an unsigned, 32-bit binary, this is: 00000000000000000000000000000001
You flip its bits: 11111111111111111111111111111110
Which in decimal is: 4294967294
"""


def flipping_bits(x):

    convert_to_bin = bin(x)[2:].zfill(32) # x is a string here
    #flip the 1's and 0's, using a placeholder 'y' for '1'
    flip = convert_to_bin.replace('1', 'y').replace('0', '1').replace('y', '0')
    return int(flip, 2)

number_of_entries = list(input())

if __name__ == '__main__':
    num_tests = int(input())

    for _ in range(num_tests):
        number = int(input())
        answer = flipping_bits(number)
        print(answer)