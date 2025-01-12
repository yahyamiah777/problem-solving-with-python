#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

#slice(start, end, step)


def timeConversion(s):
    # Write your code here
    
    time_type = s[-2:] #slice of the everything but the end by 2
    hour = s[:2] #slice of the front by 2
    
    if time_type == "PM" and int(hour) < 12:
        s = s[:-2] #slice without the end by 2
        new_hour = str(int(hour) + 12)
        result = new_hour + s[2:] #slice without the front by 2
        return result
    elif time_type == "AM" and int(hour) == 12:
        s = s[:-2]
        new_hour = "00"
        result = new_hour + s[2:]
        return result
    else:
        s = s[:-2]
        result = s
        return result
        
    
s = "07:05:45AM"

timeConversion(s)