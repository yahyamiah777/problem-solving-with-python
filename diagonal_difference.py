#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    
    matrix_length = len(arr)
    
    diagonal_1 = []
    diagonal_2 = []
    
    for i in range(matrix_length):
        diagonal_1.append(arr[i][i])
        diagonal_2.append(arr[i][matrix_length-i-1]) #this makes more sense if you understand that arrays index start at 0
    
    #for a matrix of size n x n, the secondary diagonal consists of elements where the column index decreases 
    #as the row index increases. Specifically: 
    
    #For row 0, the column index is n-1.
    #For row 1, the column index is n-2.
    #For row 2, the column index is n-3.

    total_1 = sum(diagonal_1)
    total_2 = sum(diagonal_2)
    return abs(total_1-total_2)
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
