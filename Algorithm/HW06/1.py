import heapq

def solution(scoville, K):
    # scoville 리스트를 최소 힙으로 변환
    heapq.heapify(scoville)
    shake_num = 0

    # 가장 작은 스코빌 지수가 K 이상이 될 때까지 음식을 섞음
    while scoville[0] < K:
        # 음식이 2개 미만인 경우 모든 음식을 섞어도 K 이상이 되지 못하므로 -1을 반환
        if len(scoville) < 2:
            return -1
        # 가장 작은 두 개의 음식을 가져와서 섞은 음식을 만듦
        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new_food = first + (second * 2)
        # 섞은 음식을 다시 힙에 추가
        heapq.heappush(scoville, new_food)
        # 섞은 횟수를 카운트
        shake_num += 1

    return shake_num
