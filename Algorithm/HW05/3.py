def solution(prices):
    answer = [0] * len(prices)  # 가격이 떨어지지 않은 기간을 저장하는 배열
    stack = []  # 인덱스를 저장하는 스택

    for i in range(len(prices)):
        # 스택이 비어있지 않고, 현재 가격이 스택의 가장 위에 있는 가격보다 작을 경우
        while stack and prices[i] < prices[stack[-1]]:
            j = stack.pop()  # 스택의 가장 위에 있는 인덱스를 가져옴
            answer[j] = i - j  # 현재 시점에서 스택의 가장 위에 있는 인덱스를 뺀 값을 저장 (가격이 떨어진 기간)
        stack.append(i)  # 현재 인덱스를 스택에 추가

    # 스택에 남아있는 인덱스들에 대해 마지막 시점과의 차이를 계산하여 저장
    while stack:
        j = stack.pop()
        answer[j] = len(prices) - 1 - j

    return answer
