# 베스트 앨범: https://school.programmers.co.kr/learn/courses/30/lessons/42579

def solution(genres, plays):
    answer = []
    dic = {}
    
    # 각 장르별로 재생 횟수 합계를 계산합니다.
    for i in range(len(genres)):
        genre, play = genres[i], plays[i]
        if genre in dic:
            dic[genre]['play_sum'] += play
            dic[genre]['songs'].append((play, i))
        else:
            dic[genre] = {'play_sum': play, 'songs': [(play, i)]}
            
    # {'classic': {'play_sum': 1450, 'songs': [(500, 0), (150, 2), (800, 3)]}, 'pop': {'play_sum': 3100, 'songs': [(600, 1), (2500, 4)]}}
    # 재생 횟수에 따라 각 장르별 노래를 내림차순으로 정렬합니다.
    for genre in sorted(dic.keys(), key=lambda x: dic[x]['play_sum'], reverse=True):
        songs = dic[genre]['songs']
        songs = sorted(songs, key=lambda x: x[0], reverse=True)
        # [(2500, 4), (600, 1)]
        # [(800, 3), (500, 0), (150, 2)]

        # 각 장르별로 노래를 2개씩 선택합니다.
        for i in range(min(len(songs), 2)):
            answer.append(songs[i][1])

    return answer
