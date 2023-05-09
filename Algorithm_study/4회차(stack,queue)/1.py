# 같은 숫자는 싫어 : https://school.programmers.co.kr/learn/courses/30/lessons/12906 

def solution(arr):
    answer = [arr[0]]
    
    for i in range(1, len(arr)):
        if arr[i] != arr[i-1]:
            answer.append(arr[i])
            
    return answer


def solution_2(arr):
    answer = [arr[0]]

    for i in arr:
        if answer[-1] == i:
            continue
        answer.append(i)

    return answer