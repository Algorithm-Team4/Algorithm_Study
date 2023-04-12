def solution(nums):
    ponketmon_dictionary = {}
    answer = 0
    if (len(nums) % 2 == 0) :
        limit_checker = len(nums) / 2
    else :
        limit_checker = len(nums) / 2 + 1

    for ponketmon in nums :
        if ponketmon in ponketmon_dictionary :
            ponketmon_dictionary[ponketmon] += 1
        else :
            ponketmon_dictionary[ponketmon] = 1
    
    if len(ponketmon_dictionary) <= limit_checker :
        answer = len(ponketmon_dictionary)
    else :
        answer = limit_checker
    return answer