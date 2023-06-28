import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while scoville[0] < K:
        if len(scoville) == 1:
            return -1
        new_scoville = heapq.heappop(scoville) + heapq.heappop(scoville) * 2
        heapq.heappush(scoville, new_scoville)
        answer += 1
    
    return answer

#처음 while 조건문에 new_scoville을 넣었었음 이렇게 될경우 new_scoville이 항상 루트노트(제일작은값)이 아니기 때문에 에러가 발생함 
