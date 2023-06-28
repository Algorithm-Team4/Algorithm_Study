import heapq

def solution(jobs):
    total = 0
    cur_time = 0
    n = len(jobs)
    jobs.sort(key=lambda x: x[0]) # 요청 시간으로 정렬
    heap = []

    while jobs or heap:
        while jobs and jobs[0][0] <= cur_time:
            heapq.heappush(heap, jobs.pop(0)[::-1])

        if not heap:
            cur_time = jobs[0][0]
            continue

        process = heapq.heappop(heap)
        cur_time += process[0]
        total += cur_time - process[1]

    return total // n