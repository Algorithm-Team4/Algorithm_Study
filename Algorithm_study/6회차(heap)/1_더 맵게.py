# https://school.programmers.co.kr/learn/courses/30/lessons/42626


# 시간 초과
from collections import deque

def solution(scoville, K):
    scoville = deque(sorted(scoville))
    cnt = 0
    while scoville[0] < K:
        if len(scoville) < 2:
            return -1
        mix = scoville.popleft() + scoville.popleft() * 2
        scoville.append(mix)
        scoville = sorted(scoville)
        cnt += 1
    return cnt

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 힙으로 변환
    cnt = 0
    while scoville[0] < K:  # 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
        if len(scoville) < 2:  # 모든 음식의 스코빌 지수를 K 이상으로 만들 수 없는 경우에는 -1을 retrun
            return -1
        mix = heapq.heappop(scoville) + heapq.heappop(scoville) * 2  # 가장 작은 두 스코빌 지수를 섞음
        heapq.heappush(scoville, mix)  # 섞은 음식을 힙에 추가
        cnt += 1
    return cnt