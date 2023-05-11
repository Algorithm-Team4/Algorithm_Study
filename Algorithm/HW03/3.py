def solution(genres, plays):
    genre_play_dict = {}
    genre_songs_dict = {}

    #조건 1 : 속한 노래가 많이 재생된 장르를 먼저 수록합니다.
    #조건 2 : 장르 내에서 많이 재생된 노래를 먼저 수록합니다.
    #조건 3 : 장르 내에서 재생 횟수가 같은 노래 중에서는 고유 번호가 낮은 노래를 먼저 수록합니다.
    for i in range(len(genres)):
        genre = genres[i]
        play = plays[i]
        #없을 경우 초기화
        if genre not in genre_play_dict:
            genre_play_dict[genre] = 0
            genre_songs_dict[genre] = [(-1, -1), (-1, -1)]
            #해당 장르의 가장 많이 재생된 (곡의 번호, 재생 수) ==> 초기 값은 음수로 해서 확실하게 바꿀 수 있게
            #두번째로 가장 많이 재생된 (곡의 번호, 재생 수)

        genre_play_dict[genre] += play
        #해당 장르 키(노래)에 해당 되는 재생 수를 업데이트
        
        if play > genre_songs_dict[genre][0][1]:
            genre_songs_dict[genre][1] = genre_songs_dict[genre][0]
            genre_songs_dict[genre][0] = (i, play)
        elif play > genre_songs_dict[genre][1][1]:
            genre_songs_dict[genre][1] = (i, play)

    genre_rank = list(genre_play_dict.keys())
    print(genre_play_dict)
    genre_rank.sort(key=lambda x: genre_play_dict[x], reverse=True)
    print(genre_rank)
    #play가 높은 순으로 오도록 정렬

    answer = []
    for genre in genre_rank:
        for song in genre_songs_dict[genre]: 
            if song[0] != -1:
                answer.append(song[0])

    return answer

# 테스트 케이스
print(solution(["classic", "pop", "classic", "classic", "rock"], [500, 600, 150, 800, 2500]))  # [4, 1, 3, 0]

