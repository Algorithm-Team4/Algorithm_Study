import heapq

def solution(operations):
    min_heap = []  # 최솟값을 저장하는 최소 힙
    max_heap = []  # 최댓값을 저장하는 최대 힙

    for operation in operations:
        op, num = operation.split()  
        # 명령어와 숫자 분리
        num = int(num)

        if op == 'I':  # 삽입 연산인 경우
            heapq.heappush(min_heap, num)  # 최소 힙에 삽입
            heapq.heappush(max_heap, -num)  # 최대 힙에 음수로 변환하여 삽입
            
        elif op == 'D':  # 삭제 연산인 경우
            if num == 1:  # 최댓값 삭제
                if max_heap:  # 최대 힙이 비어있지 않은 경우
                    heapq.heappop(max_heap)  # 최댓값 삭제
                    # 최댓값 삭제 시 최소 힙에서도 동일한 값을 삭제해야 함
                    min_heap = [-x for x in max_heap]
                    heapq.heapify(min_heap)
            elif num == -1:  # 최솟값 삭제
                if min_heap:  # 최소 힙이 비어있지 않은 경우
                    heapq.heappop(min_heap)  # 최솟값 삭제
                    # 최솟값 삭제 시 최대 힙에서도 동일한 값을 삭제해야 함
                    max_heap = [-x for x in min_heap]
                    heapq.heapify(max_heap)

    if not min_heap:  # 큐가 비어있는 경우
        return [0, 0]
    else:
        return [-max_heap[0], min_heap[0]]  # 최댓값과 최솟값 반환
