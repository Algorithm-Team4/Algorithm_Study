# 올바른 괄호 : https://school.programmers.co.kr/learn/courses/30/lessons/12909

def solution(s):
    stack = []

    for i in s:
        #  '('는 append
        if i == '(':
            stack.append(i) 
        #   ')'는 pop
        else: 
            # 비어있는 경우 올바르지 않음
            if not stack:
                return False 
            stack.pop()
    # 스택에 값이 있을 경우: False
    # 스택에 값이 없을 경우: True
    return not stack


def solution_2(s): 
    # '(' 1로 치환 , ')' -1로 치환
    dict = {'(': 1, ')': -1}
    answer = 0
    # s 순회하면서 answer값에 치환값을 더해주면서
    for i in s:
        answer += dict[i]
        # 열려있지도 않은데 먼저 닫힐경우 False
        if answer < 0:
            return False
        # '(' , ')' 의 개수가 같으면 True
        return True if answer == 0 else False
