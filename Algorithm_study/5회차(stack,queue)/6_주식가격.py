# 주식 가격: https://school.programmers.co.kr/learn/courses/30/lessons/42584

# O(n^2)
def solution(prices):
    n = len(prices)
    answer = [0] * n
    
    for i in range(n):
        for j in range(i+1, n):
            if prices[i] <= prices[j]:
                answer[i] += 1
            else:
                answer[i] += 1
                break
    return answer

# O(n^2)
from collections import deque

def solution(prices):
    answer = []
    prices = deque(prices)

    while prices:
        p = prices.popleft()
        time = 0
        for i in prices:
            time += 1
            if p > i:
                break
        answer.append(time)
    
    return answer
 
 # O(n)
def solution(prices):
    n = len(prices)
    answer = [0] * n
    stack = [] # 인덱스 저장

    for i in range(n):
        while stack and prices[stack[-1]] > prices[i]:
            idx = stack.pop()
            answer[idx] = i - idx
        stack.append(i)
    # stack = [0, 1, 3, 4]
    # answer = [0, 0, 1, 0, 0]

    # stack에 남아있는 값들 pop    
    while stack:
        idx = stack.pop()
        answer[idx] = n - idx - 1
    return answer # [4,3,1,1,0]