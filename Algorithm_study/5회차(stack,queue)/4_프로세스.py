#  프로세스 : https://school.programmers.co.kr/learn/courses/30/lessons/42587


# 시간 복잡도 : O(n^2)
from collections import deque

def solution(priorities, location):
    queue =  deque([(val,idx) for idx,val in enumerate(priorities)])
    # priorities = [2, 1, 3, 2] -> [(2,0), (1,1), (3,2), (2,3)]
    answer = 0

    # queue가 빈 상태가 아닐 때까지 반복
    while queue:
        
        max_q = max(queue)
        # 실행 대기 큐(Queue)에서 대기중인 프로세스 하나를 꺼냅니다.  
        process = queue.popleft()

        if max_q[0] > process[0]: # 큐에 대기중인 프로세스 중 우선순위가 더 높은 프로세스가 있다면 
            queue.append(process) # 방금 꺼낸 프로세스를 다시 큐에 넣습니다.
        else:
            # 만약 그런 프로세스가 없다면 방금 꺼낸 프로세스를 실행합니다.
            answer += 1
            # 몇 번째로 실행되는지 알고싶은 프로세스의 위치
            if process[1] == location:
                return answer
