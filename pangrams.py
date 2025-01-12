#!/bin/python3

import math
import os
import random
import re
import sys
import string

#
# Complete the 'pangrams' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def pangrams(s):
    # Write your code here
    alphabet = set(string.ascii_lowercase) #{'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}

    #a set is an unordered collection of unique elements

    #string.ascii_lowercase is a Python constant that contains all lowercase English letters 
    #as a string: 'abcdefghijklmnopqrstuvwxyz'.
    
    if (set(s.lower()) >= alphabet): #does it contain at least all the letters in the alphabet
        return "pangram"
    else:
        return "not pangram"
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = pangrams(s)

    fptr.write(result + '\n')

    fptr.close()
