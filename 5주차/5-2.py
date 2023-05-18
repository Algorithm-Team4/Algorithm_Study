import queue

def solution(bridge_length, weight, truck_weights):
    bridge_queue = queue.Queue()
    bridge_weight = 0
    time = 0

    for truck in truck_weights:
        if bridge_queue.qsize() >= bridge_length:
            bridge_weight -= bridge_queue.get()

        tmp_weight = bridge_weight + truck
        time += 1
        while tmp_weight > weight:
            bridge_queue.put(0)
            if bridge_queue.qsize() >= bridge_length:
                tmp_weight -= bridge_queue.get()
            time += 1

        bridge_queue.put(truck)
        bridge_weight = tmp_weight

    return time + bridge_length
