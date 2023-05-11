def solution(arr):
    answer = []
    answer.append(arr[0])
    #zero index 피하기

    for num in arr :
        if (num != answer[-1]) :
            #배열의 맨 끝이 다르면 num을 입력
            answer.append(num)    
    return answer