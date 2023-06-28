import heapq

def solution(operations):
    heap = []
    
    for i in operations:
        if i[0] == 'I':
            heapq.heappush(heap, int(i[2:]))            
        else:
            if not heap:
                continue
            if i[2] == "-":
                heapq.heappop(heap)
            else:
                heap.pop(heap.index(heapq.nlargest(1, heap)[0]))                
    if not heap:
        return [0, 0]
    else:
        return [heapq.nlargest(1, heap)[0], heap[0]]