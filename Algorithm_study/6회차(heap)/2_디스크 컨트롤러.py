import heapq

def solution(jobs):
    total = 0
    job_idx = 0
    cur_time = 0
    jobs.sort(key=lambda x: x[0]) # 요청 시간으로 정렬
    heap = []

    while j < len(jobs) or heap:
        if j < len(jobs) and cur_time >= jobs[j][0]:
            heapq.heappush(heap, (jobs[j][1], jobs[j][0]))
            j += 1
            continue

        if heap:
            job = heapq.heappop(heap)
            cur_time += job[0]
            total += cur_time - job[1]
        else:
            cur_time = jobs[j][0]

    return total // len(jobs)

import heapq

def solution(jobs):
    total = 0
    
    cur_time = 0
    
    jobs.sort(key=lambda x: x[0])

    heap = []

    while heap:
        for request, processing in jobs:
            if cur_time >= request:
                heapq.heappush(heap, (processing, request))

        if heap:
            processing, request = heapq.heappop(heap)
            cur_time += processing
            total += cur_time - request
        else:
            cur_time = 
            
