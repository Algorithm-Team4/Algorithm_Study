import heapq

heapq.heapify(x)  # x 리스트를 힙으로 변환 (in-place)

heapq.heappush(heap, item)  # heap에 item 값을 추가

heapq.heappop(heap)  # heap에서 가장 작은 항목 제거 및 반환

heapq.heappushpop(heap, item)  # heap에 item 값을 추가하고 가장 작은 항목 반환

heapq.heapreplace(heap, item)  # heap에서 가장 작은 항목 제거하고 item 값을 추가

heapq.merge(*iterables, key=None, reverse=False)  # 여러 정렬된 입력을 하나의 정렬된 출력으로 병합

heapq.nlargest(n, iterable, key=None)  # iterable에서 가장 큰 n개의 요소로 구성된 리스트 반환

heapq.nsmallest(n, iterable, key=None)  # iterable에서 가장 작은 n개의 요소로 구성된 리스트 반환