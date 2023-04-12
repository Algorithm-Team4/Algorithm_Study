def solution(x, n):
    if ( x < -10000000 or x > 10000000) :
        return -1
    if (n > 1000) :
        return -1
    
    answer = []
    tmp_num = 0
    for i in range(0, n) :
        tmp_num += x
        answer.append(tmp_num)
    return answer