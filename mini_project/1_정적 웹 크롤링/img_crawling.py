import requests
from urllib.request import urlretrieve
from bs4 import BeautifulSoup as bs
import os

# 1. 네이버에 고양이를 검색한 뒤 이미지 탭을 누른 url을 요청
url = requests.get(f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4")

# 2. BeautifulSoup을 사용하여 HTML 콘텐츠를 추출
soup = bs(url.text, 'html.parser')

# 3. img 태그를 추출하여 이미지 URL 가져오기
imgs = soup.select('img')
src = [i.get('src') for i in imgs]

# 4. 저장할 폴더 생성
if not os.path.exists('mini_project/1_정적 웹 크롤링/img'):
    os.makedirs('mini_project/1_정적 웹 크롤링/img')

for i in range(10) : # .jpg 이미지 파일로 10장 저장
    urlretrieve(src[i], f'mini_project/1_정적 웹 크롤링/img/cat_{i+1}.jpg')