#!/bin/python3

import math
import os
import random
import re
import sys



#
# Complete the 'reverseArray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#

def reverseArray(arr):
    return arr[::-1]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = []

    for i in range(arr_count):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = reverseArray(arr)

    print(result)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
