def solution(progresses, speeds):
    answer = []
    day = 0
    patch_list = 0
    
    #조건1 : 앞의 작업이 끝나야 뒤의 작업이 패치에 반영
    #조건2 : 작업도 + 진행속도 * 시간 >= 100이 되어야 패치에 반영
    # ==>날짜의 경과에 따라 첫번째 작업부터 완료된 것을 추적
    # ==>다 된 작업은 pop해서 삭제 == 완료한 일정을 지움 
    while len(progresses) > 0:
        if (progresses[0] + day * speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            patch_list += 1
        else:
            if patch_list > 0:
                answer.append(patch_list)
                patch_list = 0
            day += 1
    answer.append(patch_list)
    return answer
