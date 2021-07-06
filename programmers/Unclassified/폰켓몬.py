# 출처: 프로그래머스 코딩 테스트 연습, https://programmers.co.kr/learn/challenges
def solution(nums):
    max_pick = len(nums) // 2
    total_species = len(set(nums))
    return min(total_species, max_pick)
