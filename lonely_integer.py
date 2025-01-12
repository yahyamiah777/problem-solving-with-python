#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'lonelyinteger' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def lonelyinteger(a):
    # Write your code here
    
    result = [i for i in a if a.count(i) <2] #list comprehension
    
    return result[0]

# or

from collections import Counter

def lonelyinteger2(a):
    # Create a frequency counter for the elements in 'a'
    count = Counter(a)
    
    # Find the element that appears only once
    for num, freq in count.items():
        if freq == 1:
            return num

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = lonelyinteger(a) #or result = lonelyinteger2(a)
    

    fptr.write(str(result) + '\n')

    fptr.close()
