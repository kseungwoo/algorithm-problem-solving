import re


def solution(dartResult):
    nums = list(map(int, re.findall(r'\d+', dartResult)))
    ni = 0
    for i, c in enumerate(dartResult):
        if c in ('S', 'D', 'T'):
            if c == 'D':
                nums[ni] **= 2
            if c == 'T':
                nums[ni] **= 3
            if i + 1 < len(dartResult):
                if dartResult[i + 1] == '*':
                    if ni > 0:
                        nums[ni - 1] *= 2
                    nums[ni] *= 2
                if dartResult[i + 1] == '#':
                    nums[ni] = -nums[ni]
            ni += 1
    return sum(nums)
