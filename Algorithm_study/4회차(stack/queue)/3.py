#  기능개발: https://school.programmers.co.kr/learn/courses/30/lessons/42586

def solution(progresses, speeds):
    days = []
    answer = []
    
    for i in range(len(progresses)):
        day = -(-(100-progresses[i]) // speeds[i]) # 올림
        days.append(day)
    print(days)
    # [5, 10, 1, 1, 20, 1]

    maxday_idx = 0 # 작업일수가 큰 인덱스
    for i in range(len(days)):
        if days[i] > days[maxday_idx]:
            answer.append(i - maxday_idx)
            maxday_idx = i
    answer.append(len(days) - maxday_idx)
    
    return answer # [1, 3, 2]