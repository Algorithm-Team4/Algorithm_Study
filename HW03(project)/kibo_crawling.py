import os
import requests
from bs4 import BeautifulSoup

# 사용자로부터 플레이어 이름을 입력받음
player_name = input("Enter the player's name: ")

# 검색 URL 생성
search_url = f'http://gokifu.com/ko/?q={requests.utils.quote(player_name)}&p='

# '플레이어이름' 디렉토리가 없으면 생성
if not os.path.exists(player_name):
    os.makedirs(player_name)

# 파일을 다운로드하여 지정된 경로에 저장하는 함수
def file_save(link, file):
    try:
        response = requests.get(link)
        with open(file, 'wb') as save_file:
            save_file.write(response.content)
    except Exception as e:
        print(e)

# 사용자로부터 마지막 페이지 번호를 입력받음
last_page = int(input("Enter the last page number: "))

# 지정된 페이지 범위 내에서 크롤링 수행
for page in range(1, last_page + 1):
    numbering_url = search_url + str(page)
    response = requests.get(numbering_url)
    
    # 웹 페이지를 파싱하여 BeautifulSoup 객체 생성
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # "game_type" 클래스를 가진 div 태그를 모두 찾음
    table = soup.find_all("div", {"class": "game_type"})

    # 각 div 태그 내의 sgf 파일 링크를 찾음
    for item in table:
        link_tag = item.find('a')
        if link_tag:
            link = link_tag['href']
            # 파일 이름 추출 후 확장명을 .sgf로 변경
            file_name = link.split('/')[-1].replace('.html', '.sgf')
            save_path = f'{player_name}/{file_name}'

            # 해당 파일이 아직 저장되지 않았다면 다운로드하고 저장
            if not os.path.exists(save_path):
                file_save(link, save_path)
