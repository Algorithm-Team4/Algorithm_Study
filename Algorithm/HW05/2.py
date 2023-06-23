from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0  # 현재 시간
    bridge = deque()  # 다리에 올라가 있는 트럭과 해당 트럭이 다리를 건넌 시간을 저장하는 큐
    truck_queue = deque([(w, 0) for w in truck_weights])  # 트럭의 무게와 시간을 저장하는 큐

    while True:
        # 다리에 있는 트럭 관리
        if bridge:
            if time - bridge[0][1] >= bridge_length:  # 가장 먼저 올라간 트럭이 다리를 모두 건넜는지 확인
                bridge.popleft()

        # 다리에 트럭이 올라갈 수 있는 경우
        if truck_queue:
            if sum([t[0] for t in bridge]) + truck_queue[0][0] <= weight:  # 다음 트럭이 다리에 올라갈 수 있는지 확인
                truck = truck_queue.popleft()
                bridge.append((truck[0], time))

        # 현재 시간 증가
        time += 1

        # 다리에 트럭이 없으면 종료
        if not bridge:
            break

    return time
