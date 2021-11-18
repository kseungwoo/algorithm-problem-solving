#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'getWinnerTotalGoals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING competition
#  2. INTEGER year
#
import requests


def getHomeTotalPages(competition, team, year):
    response = requests.get(
        "https://jsonmock.hackerrank.com/api/football_matches?competition=%s&year=%d&team1=%s&page=1" % (
        competition, year, team))
    return response.json()["total_pages"]


def getHomeTotalGoals(competition, team, year):
    total_goals = 0
    total_pages = getHomeTotalPages(competition, team, year)
    for page in range(1, total_pages + 1):
        response = requests.get(
            "https://jsonmock.hackerrank.com/api/football_matches?competition=%s&year=%d&team1=%s&page=%d" % (
            competition, year, team, page))
        for play in response.json()["data"]:
            total_goals += int(play["team1goals"])
    return (total_goals)


def getAwayTotalPages(competition, team, year):
    response = requests.get(
        "https://jsonmock.hackerrank.com/api/football_matches?competition=%s&year=%d&team2=%s&page=1" % (
        competition, year, team))
    return response.json()["total_pages"]


def getAwayTotalGoals(competition, team, year):
    total_goals = 0
    total_pages = getAwayTotalPages(competition, team, year)
    for page in range(1, total_pages + 1):
        response = requests.get(
            "https://jsonmock.hackerrank.com/api/football_matches?competition=%s&year=%d&team2=%s&page=%d" % (
            competition, year, team, page))
        for play in response.json()["data"]:
            total_goals += int(play["team2goals"])
    return (total_goals)


def getTotalGoals(competition, team, year):
    return getHomeTotalGoals(competition, team, year) + getAwayTotalGoals(competition, team, year)


def getWinner(competition, year):
    response = requests.get(
        "https://jsonmock.hackerrank.com/api/football_competitions?name=%s&year=%d" % (competition, year))
    print(response.json())
    return response.json()["data"][0]["winner"]


def getWinnerTotalGoals(competition, year):
    winner = getWinner(competition, year)
    return getTotalGoals(competition, winner, year)
    # Write your code here
    # https://jsonmock.hackerrank.com/api/football_competitions?name=English Premier League&year=2014
    # https://jsonmock.hackerrank.com/api/football_matches?competition


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    competition = input()

    year = int(input().strip())

    result = getWinnerTotalGoals(competition, year)

    fptr.write(str(result) + '\n')

    fptr.close()
