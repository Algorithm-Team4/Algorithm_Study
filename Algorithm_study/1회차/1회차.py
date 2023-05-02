'''
평균 구하기 : https://school.programmers.co.kr/learn/courses/30/lessons/12944
짝수와 홀수 : https://school.programmers.co.kr/learn/courses/30/lessons/12937
약수의 합 : https://school.programmers.co.kr/learn/courses/30/lessons/12928
자릿수 더하기 : https://school.programmers.co.kr/learn/courses/30/lessons/12931
x만큼 간격이 있는 n개의 숫자 : https://school.programmers.co.kr/learn/courses/30/lessons/12954
문자열 내 p와 y의 개수 : https://school.programmers.co.kr/learn/courses/30/lessons/12916
나머지가 1이 되는 수 찾기 : https://school.programmers.co.kr/learn/courses/30/lessons/87389
'''

# 평균 구하기
def solution_1(arr):
    return sum(arr) / len(arr)

# 짝수와 홀수
def solution_2(num):
    return 'Odd' if num % 2 == 1 else 'Even'

# 약수의 합
def solution_3(n):
    return sum([i for i in range(1, n+1) if n % i == 0])

# 자릿수 더하기
def solution_4(n):
    strn = str(n)
    sum = 0
    for i in strn:
        sum += int(i)
    return sum

# x만큼 간격이 있는 n개의 숫자
def solution_5(x, n):
    if x == 0:
        return [0]*n
    elif x > 0:
        return list(range(x, n*x+1, x))
    else:
        return sorted(list(range(n*x, x+1, -x)), reverse=True)      

# 문자열 내 p와 y의 개수
def solution_6(s):
    s = s.lower()
    if s.count('p') == s.count('y'):
        return True
    else:
        return False

# 나머지가 1이 되는 수 찾기
def solution_7(n):
    for i in range(2, n):
        if n % i == 1:
            return i