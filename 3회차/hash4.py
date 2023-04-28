# 의상 : https://school.programmers.co.kr/learn/courses/30/lessons/42578

# O(n) 
def solution(clothes):
    answer = 1
    hash_dict = {}
    
    # clothes 리스트를 순회하며, 각 옷 종류(c_kind)에 해당하는 옷 이름(c_name)을 hash_dict 딕셔너리에 추가합니다.
    for c_name, c_kind in clothes:
        if c_kind in hash_dict:
            hash_dict[c_kind].append(c_name)
        else:
            hash_dict[c_kind] = [c_name]
    
    # hash_dict 딕셔너리의 모든 키(key)에 대해, (해당 옷 종류의 개수 + 1)을 answer에 곱해줍니다.
    for key in hash_dict.keys():
        answer *= (len(hash_dict[key]) + 1)
    
    # 모든 경우의 수에서 아무것도 입지 않은 경우를 빼줍니다.
    answer -= 1
    
    return answer