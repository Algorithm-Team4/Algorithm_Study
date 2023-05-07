# 완주하지 못한 선수: https://school.programmers.co.kr/learn/courses/30/lessons/42576

def solution_1(participant, completion):
    for i in completion:
        participant.remove(i)
        
    return participant[0]

'''
효울성 테스트

테스트 1 〉	실패 (시간 초과)
테스트 2 〉	실패 (시간 초과)
테스트 3 〉	실패 (시간 초과)
테스트 4 〉	실패 (시간 초과)
테스트 5 〉	실패 (시간 초과)
'''

def solution_2(participant, completion):
    answer = ''

    participant.sort()
    completion.sort()

    for i in range(len(completion)):
        if(participant[i] != completion[i]):
           return participant[i]
    
    return participant[-1]
'''
효율성 테스트

테스트 1 〉	통과 (43.64ms, 18.1MB)
테스트 2 〉	통과 (59.08ms, 22.1MB)
테스트 3 〉	통과 (70.08ms, 24.8MB)
테스트 4 〉	통과 (78.77ms, 26.2MB)
테스트 5 〉	통과 (74.90ms, 26.2MB)
'''

def solution_3(participant, completion):
    dict = {}
    sum = 0

    for p in participant:
        dict[hash(p)] = p
        sum += hash(p)
    
    for c in completion:
        sum -= hash(c)
    
    return dict[sum]

'''
효율성  테스트

테스트 1 〉	통과 (20.32ms, 23.7MB)
테스트 2 〉	통과 (32.40ms, 28.4MB)
테스트 3 〉	통과 (41.36ms, 31.4MB)
테스트 4 〉	통과 (48.55ms, 37.6MB)
테스트 5 〉	통과 (89.84ms, 37.6MB)
'''