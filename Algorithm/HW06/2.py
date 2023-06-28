import heapq

def solution(jobs):
    jobs.sort(key=lambda x: x[0])  # 작업을 요청한 시점을 기준으로 정렬
    n = len(jobs)  # 작업의 개수
    total_time = 0  # 총 대기 시간
    current_time = 0  # 현재 시간
    heap = []  # 작업을 처리하기 위한 힙

    while jobs or heap:
        # 현재 시간 이전에 요청된 작업들을 힙에 추가
        while jobs and jobs[0][0] <= current_time:
            request_time, duration = jobs.pop(0)
            heapq.heappush(heap, (duration, request_time))

        if heap:
            # 힙에서 소요 시간이 가장 작은 작업을 가져와서 처리
            duration, request_time = heapq.heappop(heap)
            start_time = max(current_time, request_time)  # 작업 시작 시간
            current_time = start_time + duration  # 작업 완료 시간
            total_time += current_time - request_time  # 대기 시간 누적
        else:
            # 힙이 비어있는 경우, 다음 작업의 요청 시점으로 시간을 이동
            current_time = jobs[0][0]

    return total_time // n
