def solution(clothes):
    clothes_Dictionary = {}

    for cloth, category in clothes :
        if category in clothes_Dictionary :
            clothes_Dictionary[category].append(cloth)
        else :
            clothes_Dictionary[category] = [cloth]
    answer = 1

    for category in clothes_Dictionary :
        answer *= (len(clothes_Dictionary[category]) + 1)

    return answer - 1

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) 
# 정답 : 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) 
# 정답 : 3