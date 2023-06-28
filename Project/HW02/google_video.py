from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By
from urllib.parse import quote_plus

#step2.검색할 키워드 입력
query = input('검색어를 입력하세요: ')

#step3.크롬드라이버로 원하는 url로 접속
driver = webdriver.Chrome('/path/to/chromedriver')
baseUrl = 'https://www.google.com/search?q='

url = baseUrl + quote_plus(query)
#위는 전역변수로 저장된 걸 불러오는 상대 경로로, 원 경로로 해도 괜찮다

driver.get(url)

time.sleep(2)

#step5.탭 클릭
driver.find_element(By.XPATH,'//*[@id="hdtb-msb"]/div[1]/div/div[4]').click()

time.sleep(2)

#step8.탭 경로 썸네일 영상 추출
thumbnail = driver.find_elements(By.CSS_SELECTOR, "g-inner-card")

link_thumbnail = []

for a in thumbnail:
    link_thumbnail.append(a.get_attribute('href'))


# 저장할 폴더 생성
import os

# path_folder의 경로는 각자 저장할 폴더의 경로를 적어줄 것(ex.img_download)
path_folder = 'C:/Users/ykeng/Desktop/4학년 1학기/네트워크프로그래밍/python algorithm/class room homework/HW02'

if not os.path.isdir(path_folder):
    os.mkdir(path_folder)


# 이미지 다운로드

from urllib.request import urlretrieve

i = 0

for link in link_thumbnail:          
    i += 1
    urlretrieve(link, path_folder + f'{i}.mp4')        #link에서 이미지 다운로드, './imgs/'에 파일명은 index와 확장자명으로
    if (i == 1) :
        break
time.sleep(3)

