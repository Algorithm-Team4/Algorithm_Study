# https://school.programmers.co.kr/learn/courses/30/lessons/42626

import heapq

def solution(scoville, K):
    heapq.heapify(scoville)  # 힙으로 변환
    cnt = 0
    while scoville[0] < K:  # 모든 음식의 스코빌 지수가 K 이상이 될 때까지 반복
        if len(scoville) < 2:  # 음식이 2개 미만이면 더 이상 섞을 수 없으므로 -1 반환
            return -1
        mixed = heapq.heappop(scoville) + heapq.heappop(scoville) * 2  # 가장 작은 두 스코빌 지수를 섞음
        heapq.heappush(scoville, mixed)  # 섞은 음식을 힙에 추가
        cnt += 1
    return cnt


