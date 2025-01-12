#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    
    min_sum =0
    max_sum =0
    arr.sort()
    
    first_array = arr[0:4]
    
    for i in first_array:
        min_sum += i
    
    second_array = arr[1:]
    for i in second_array:
        max_sum += i
        
    print(min_sum, max_sum)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
