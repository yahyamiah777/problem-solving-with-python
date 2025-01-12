#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'flippingBits' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts LONG_INTEGER n as parameter.
#

def flippingBits(n):
    # Write your code here
    return n ^ 0xFFFFFFFF # is a hexadecimal (base 16) representation of a number where all 32 bits are set to 1 so
                          # 11111111111111111111111111111111
                          # so it is a mask or could be a limiter

    # ^ is a comparison operator that follows the rules of 1 ^ 1 = 0 and 0 ^ 1 = 1,
    # which allows for the flipping of bits (n ^ and a number that represents a binary)
    
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        result = flippingBits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
