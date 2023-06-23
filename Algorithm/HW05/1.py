from collections import deque

def solution(priorities, location):
    count = 0  # 현재까지 실행한 프로세스 개수
    queue = deque([(p, i) for i, p in enumerate(priorities)])  # (우선순위, 위치)로 대기 큐 생성

    while queue:
        front = queue.popleft()
        if any(front[0] < p[0] for p in queue):  # 더 높은 우선순위가 있는지 확인
            queue.append(front)
        else:
            count += 1
            if front[1] == location:
                return count
