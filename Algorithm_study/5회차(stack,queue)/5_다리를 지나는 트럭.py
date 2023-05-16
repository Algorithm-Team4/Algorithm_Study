# 다리를 지나는 트럭: https://school.programmers.co.kr/learn/courses/30/lessons/42583

from collections import deque

def solution_1(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0] * bridge_length)
    truck_weights = deque(truck_weights)

    while bridge:
        time += 1
        bridge.popleft()
        if truck_weights:
            if sum(bridge) + truck_weights[0] <= weight:   #sum(bridge) 시간초과       
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    return time

from collections import deque

def solution_2(bridge_length, weight, truck_weights):
    time = 0
    weights_sum = 0
    bridge = deque([0] * bridge_length) 
    truck_weights = deque(truck_weights) 

    # 다리가 빈 상태가 아닐 때까지 반복
    while bridge:
        time += 1
        # 다리를 지난 트럭
        c_truck = bridge.popleft()
        weights_sum -= c_truck

        if truck_weights:
            # 다리 위 트럭들의 무게와 대기트럭의 합이 weights 이하라면
            if weights_sum + truck_weights[0] <= weight: 
                # 대기트럭을 다리에 삽입 및 weights_sum = tuck_weight ++
                truck_weight = truck_weights.popleft()
                weights_sum += truck_weight
                bridge.append(truck_weight)
                # wights 초과라면 길이를 다리 길이를 유지하기 위해 0을 삽입
            else:
                bridge.append(0)
    return time
'''
        time: 1 bridge = [0,7] weights_sum = 0-0+7  truck_weights = [4,5,6] 
        time: 2 bridge = [7,0] weights_sum = 7-0+0  truck_weights = [4,5,6]
        time: 3 bridge = [0,4] weights_sum = 7-7+4 truck_weights = [5,6]
        time: 4 bridge = [4,5] weights_sum = 4-0+5 truck_weights = [6]
        time: 5 bridge = [5,0] weights_sum = 9-4+0 truck_weights = [6]
        time: 6 bridge = [0,6] weights_sum = 5-5+6 truck_weights = []
        time: 7 bridge = [6] weights_sum = 6-0
        time: 8 bridge = [] weights_sum = 6-6 
        return time
'''

