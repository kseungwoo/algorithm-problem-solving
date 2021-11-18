#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING team
#  2. INTEGER year
#
import requests
import json


def getHomeTotalPages(team, year):
    response = requests.get(
        "https://jsonmock.hackerrank.com/api/football_matches?year=%d&team1=%s&page=1" % (year, team))
    return response.json()["total_pages"]


def getHomeTotalGoals(team, year):
    total_goals = 0
    total_pages = getHomeTotalPages(team, year)
    for page in range(1, total_pages + 1):
        response = requests.get(
            "https://jsonmock.hackerrank.com/api/football_matches?year=%d&team1=%s&page=%d" % (year, team, page))
        for play in response.json()["data"]:
            total_goals += int(play["team1goals"])
    return (total_goals)


def getAwayTotalPages(team, year):
    response = requests.get(
        "https://jsonmock.hackerrank.com/api/football_matches?year=%d&team2=%s&page=1" % (year, team))
    return response.json()["total_pages"]


def getAwayTotalGoals(team, year):
    total_goals = 0
    total_pages = getAwayTotalPages(team, year)
    for page in range(1, total_pages + 1):
        response = requests.get(
            "https://jsonmock.hackerrank.com/api/football_matches?year=%d&team2=%s&page=%d" % (year, team, page))
        for play in response.json()["data"]:
            total_goals += int(play["team2goals"])
    return (total_goals)


def getTotalGoals(team, year):
    return getHomeTotalGoals(team, year) + getAwayTotalGoals(team, year)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
