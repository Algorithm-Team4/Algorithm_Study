from bs4 import BeautifulSoup as bs
import requests

#  네이버에 '광운대'라고 검색한 뒤 뉴스를 누른 url을 요청
url = requests.get('https://search.naver.com/search.naver?where=news&sm=tab_jum&query=%EA%B4%91%EC%9A%B4%EB%8C%80')

#  BeautifulSoup을 사용하여 HTML 콘텐츠를 추출
html = bs(url.text, 'html.parser')

# 'list_news' 클래스가 있는 <ul> 요소를 찾고 'bx' 클래스가 있는 모든 <li> 요소를 가져옵니다.
news = html.find('ul', class_='list_news').find_all('li', class_='bx')

# 각 <li> 요소를 반복 하고 'news_tit' 클래스가 있는 <a> 요소를 찾고 뉴스 기사의 제목을 포함하는 'title' 속성을 가져옵니다
for i in news:
    title = i.find('a', class_='news_tit')['title']
    print(title)
