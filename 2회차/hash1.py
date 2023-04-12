# 폰켓몬: https://school.programmers.co.kr/learn/courses/30/lessons/1845

def solution_1(nums):
    uniq_nums = list(set(nums))
    if len(uniq_nums) <= len(nums) // 2:
        return len(uniq_nums)
    else:
        return len(nums) // 2

def solution_2(nums):
    answer = 0
    dict = {}
    for n in nums:
        dict[n] = 1
    return min(len(nums) // 2, len(dict))