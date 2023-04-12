def solution(arr):
    answer = 0
    if (len(arr) > 100 or len(arr) < 1) :
        return -1
    for element in arr :
        if (element > 10000 or element < - 10000) :
            return -1
        answer += element
    answer /= len(arr)
    return answer