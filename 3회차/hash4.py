# 의상 : https://school.programmers.co.kr/learn/courses/30/lessons/42578

# O(n) 
def solution(clothes):
    answer = 1
    dic = {}
    
    # 각 옷 종류(c_kind)에 해당하는 옷 이름(c_name)을 딕셔너리에 추가합니다.
    for c_name, c_kind in clothes:
        if c_kind in dic:
            dic[c_kind].append(c_name)
        else:
            dic[c_kind] = [c_name]

    # 딕셔너리의 모든 키(key)에 대해, (해당 옷 종류의 개수 + 1)을 answer에 곱해줍니다.
    for key in dic.keys():
        answer *= (len(dic[key]) + 1)
    
    # 모든 경우의 수에서 아무것도 입지 않은 경우를 빼줍니다.
    answer -= 1
    
    return answer