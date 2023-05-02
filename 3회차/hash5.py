# 베스트 앨범: https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dic = {}
    
    # 장르를 key로 value 값은 다시 딕셔너리로 play_sum 과 song을 키로 가지는 딕셔너리 생성
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre in dic:
            dic[genre]['play_sum'] += play
            dic[genre]['songs'].append((play, i))
        else:
            dic[genre] = {'play_sum': play, 'songs': [(play, i)]}
    # dic = {'classic': {'play_sum': 1450, 'songs': [(500, 0), (150, 2), (800, 3)]}, 'pop': {'play_sum': 3100, 'songs': [(600, 1), (2500, 4)]}}
    
    for genre in sorted(dic.keys(), key=lambda x: dic[x]['play_sum'], reverse=True): # play_sum 기준으로 장르 내림차순
        songs = dic[genre]['songs']
        songs = sorted(songs, key=lambda x: x[0], reverse=True) # songs 리스트에서 (튜플인덱스 0번 = 장르 내 재생된 노래) 기준 내림차순
        #songs =  [(2500, 4), (600, 1)]
 	    #         [(800, 3), (500, 0), (150, 2)]

        # 각 장르별로 노래를 1 or 2개씩 선택후 answer에 노래고유번호 append . 
        for i in range(min(len(songs), 2)):
            answer.append(songs[i][1])

    return answer