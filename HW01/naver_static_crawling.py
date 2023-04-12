import requests
import urllib.request
from bs4 import BeautifulSoup as bs

def news_title_crawlilng(query) :
    # 가져올 url 문자열로 입력
    url = f'https://search.naver.com/search.naver?where=news&sm=tab_jum&query={query}'  
    # url = 'https://search.naver.com/search.naver?where=news&sm=tab_jum&query='+'%s'%query
    # 이런 형식으로도 가능 

    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)    

    # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text

    #bs4 패키지의 함수를 이용해 html 문서를 파싱한다
    soup = bs(html_text, 'html.parser')

    #bs4 패키지의 select_one 함수와 선택자 개념을 이요해서 뉴스기사 제목을 하나 가져오는 테스트 함수
    # print(soup.select_one('a.news_tit').get_text())
    # print("\n")

    #bs4 패키지의 select 함수와 선택자 개념을 이용해서 뉴스기사 제목을 모두 가져옴
    titles = soup.select('a.news_tit')

    #저장된 뉴스기사 제목을 전부 출력
    index = 1
    for i in titles :
        titles = i.get_text()
        print(f"{index}번째 기사 : " + titles)
        index += 1

def image_parser(query) :
    url = f"https://search.naver.com/search.naver?where=image&sm=tab_jum&query={query}"

    # requests의 get함수를 이용해 해당 url로 부터 html이 담긴 자료를 받아옴
    response = requests.get(url)    

    # 우리가 얻고자 하는 html 문서가 여기에 담기게 됨
    html_text = response.text

    #bs4 패키지의 함수를 이용해 html 문서를 파싱한다
    soup = bs(html_text, 'html.parser')

    imgs = soup.select('img')
    #img._image._listImage

    index = 1
    for i in imgs :
        src = i.get('src')
        savename = f'save_by_requests{index}.png'
        urllib.request.urlretrieve(src, savename)
        index += 1
        if (index > 10) : break

        # with open(savenames, "wb") as f : #바이너리(이미지)일 경우 'wb', 텍스트일 경우 'w'
        #     f.write(mem)
        #     print("저장완료!")

query = "고양이"

news_title_crawlilng(query)

image_parser(query)