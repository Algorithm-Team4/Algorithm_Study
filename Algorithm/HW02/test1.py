def solution(nums):
    arr = []
    
    for n in nums :
        if n not in arr :
            arr.append(n)
            
    if (len(nums) % 2 == 0) :
        answer = int (len(nums) / 2)
    else :
        answer = int (len(nums) / 2) + 1

    if (len(arr) >= answer) :
        return answer
    else :
        return len(arr)
    
a = solution([3,3,3,2,2,2])
print(a)
print("Hello\n")
    