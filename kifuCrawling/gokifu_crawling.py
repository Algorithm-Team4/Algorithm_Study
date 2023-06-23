import re
import urllib.request as ur
import urllib.parse
import os
import _thread

# 플레이어 이름 입력받기
player_name = input("Enter the player's name: ")

# 검색 URL 생성
search_url = f'http://gokifu.com/en/?q={urllib.parse.quote(player_name)}&p='

pattern1 = r'<div class="game_type"><a .*?href=.*?\.sgf"  ><img src="/images/save.png" sgf>'
pattern2 = r'title=.*href="(.*?sgf)'
pattern3 = r'.*-gokifu-(.*?sgf)'

def file_save(link, file):
    now_url = link
    print(now_url)
    try:
        response = ur.urlopen(now_url)
        save_file = open(file, 'wb')
        save_file.write(response.read())
        save_file.close()
    except Exception as e:
        print(e)

if os.path.exists('gokifu'):
    pass
else:
    os.makedirs('gokifu')

def getURL(num):
    for i in range(num, num + 19):
        try:
            N_url = search_url + str(i)
            response = ur.urlopen(N_url)
            restex = response.read()
            table = re.findall(pattern1, str(restex))
            for name in table:
                if os.path.exists('gokifu/' + name + '.sgf'):
                    continue
                name = re.findall(pattern2, name)[0]
                file_save(name, 'gokifu/' + re.findall(pattern3, name)[0])
        except Exception as e:
            print(e)

n = 1
for i in range(1, 50, 20):
    try:
        _thread.start_new_thread(getURL, (i,))
        print("스레드" + str(n) + "작동 중!")
        n += 1
    except:
        print("Error: unable to start thread")

while 1:
    pass
