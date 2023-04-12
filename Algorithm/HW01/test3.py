import math
#use for sqrt(n)

def solution(n):
    answer = 0
    divisor_arr = []
    # 1 ~ sqrt(n) ==> check first divisor 
    for i in range(1, int(math.sqrt(n)) + 1) :
        if (n % i == 0) :
            divisor_arr.append(i)
            answer += i
            if (i!= n / i) :
    # check left divisor
                divisor_arr.append(n / i)
                answer += n / i
    return answer