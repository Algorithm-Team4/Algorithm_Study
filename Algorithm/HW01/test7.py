def solution(n):
    if (n > 1000000 or n < 3) :
        return -1
    answer = 0
    
    for i in range(1, n) :
        if (n % i == 1) :
            answer = i
            break
    return answer