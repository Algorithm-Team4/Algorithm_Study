import math #ceil

def solution(progresses, speeds):
    #조건1 : 앞의 작업이 끝나야 뒤의 작업이 패치에 반영
    #조건2 : 작업도 + 진행속도 * 시간 >= 100이 되어야 패치에 반영
    # ==>날짜의 경과에 따라 첫번째 작업부터 완료된 것을 추적
    # ==>다 된 작업은 pop해서 삭제 == 완료한 일정을 지움 
    answer = []
    remaining_days = []

    # 각 작업이 완료되기까지 남은 일수를 계산 progresses[i] + speeds[i] * day >= 100
    # 작업 일 >= (100% - 진행도 ) / 진행속도 ==> 최소 작업 일 = 올림((100% - 진행도) / 진행속도) 

    for i in range(len(progresses)):
        remaining_days.append(math.ceil((100 - progresses[i]) / speeds[i]))

    patch_list = 0
    current_max_day = remaining_days[0]

    # 패치되는 작업의 개수를 계산
    for day in remaining_days:
        if current_max_day < day:
            #현재 마지막 소요 날짜가 다음 작업 소요 날짜보다 낮으면 새로운 패치로
            answer.append(patch_list)
            patch_list = 1
            current_max_day = day
        else:
            #현재 소요 날짜가 다음 작업 날짜보다 많은 경우
            patch_list += 1

    answer.append(patch_list)
    return answer
