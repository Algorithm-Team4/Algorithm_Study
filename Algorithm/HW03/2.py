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
#아예 안입는 경우의 수를 제거(조건 : 최소 1개 이상의 옷을 입어야함)

print(solution([["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]])) 
# 정답 : 5
print(solution([["crow_mask", "face"], ["blue_sunglasses", "face"], ["smoky_makeup", "face"]])) 
# 정답 : 3