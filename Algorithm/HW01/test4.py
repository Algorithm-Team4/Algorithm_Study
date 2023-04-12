def solution(n):
    if (n > 100000000) :
        return -1
    
    answer = 0
    i = 1
    while (n > 0) :
        answer += n % 10
        n /= 10
        n = int(n)

    return answer