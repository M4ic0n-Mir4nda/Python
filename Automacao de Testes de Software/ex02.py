#!/bin/python3

import math
import os
import random
import re
import sys
import requests
import json



#
# Complete the 'getVoteCount' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING cityName
#  2. INTEGER estimatedCost
#  API URL: https://jsonmock.hackerrank.com/api/food_outlets?city=<cityName>&estimated_cost=<estimatedCost>
#

def getVoteCount(cityName, estimatedCost):
    response = requests.get(f"https://jsonmock.hackerrank.com/api/food_outlets?city={cityName}&estimated_cost={estimatedCost}")
    json = response.json()
    votes = 0
    if (len(json['data']) == 0):
        return -1
    for vote in json['data']:
        votes += vote['user_rating']["votes"]
    return votes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    cityName = input()

    estimatedCost = int(input().strip())

    result = getVoteCount(cityName, estimatedCost)

    fptr.write(str(result) + '\n')

    fptr.close()
