#모든 음식의 스코빌 지수를 k이상으로 하고 싶음
#스코빌 지수가 가장 낮은 음식을 아래와 같은 방법으로 섞어서 새로운 음식을 만듬
#섞은 음식의 스코빌 지수 =  가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)

def solution(scoville, K):
    scoville.sort()
    list_to_shake =[]
    shake_num = 0

    for food in scoville :
        if(food < K) :
            list_to_shake.append(food)

    # K보다 작은 음식이 존재하지 않을 경우
    if(len(list_to_shake) == 0) :
        return 0
    # K보다 작은 음식이 하나만 존재할 경우
    if(len(list_to_shake) == 1) :
        return 1

    while(True) :
        if(len(list_to_shake) < 2) :
            break
        else :
            n_food = list_to_shake[0] + list_to_shake[1] * 2
            list_to_shake.pop(0)
            list_to_shake.pop(0)
            
            shake_num +=1

            if(n_food < K) :
                list_to_shake.append(n_food)
                list_to_shake.sort()

    # 작업 후 K보다 작은 음식이 존재하지 않을 경우
    if(len(list_to_shake) == 0) :
        return shake_num
    # 작업 후 K보다 작은 음식이 하나만 남았을 경우
    if(len(list_to_shake) == 1) :
        return shake_num + 1