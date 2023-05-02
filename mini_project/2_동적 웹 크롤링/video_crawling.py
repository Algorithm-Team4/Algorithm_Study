from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from urllib.request import urlretrieve
import time
import os

# 웹 드라이버 실행
driver = webdriver.Chrome('chromedriver')

# 구글 검색 페이지 열기
driver.get('https://www.google.com/')

# 검색어 입력하기
search_box = driver.find_element(By.NAME, "q")
search_box.send_keys('코로나')
search_box.send_keys(Keys.RETURN)

# 동영상 탭으로 이동하기
driver.find_element(By.LINK_TEXT,'동영상').click()
time.sleep(3)

# 썸네일 영상 추출
thumbnails = driver.find_elements(By.CSS_SELECTOR, 'div.VYkpsb')

link_thumbnail = []
for thumbnail in thumbnails:
    link = thumbnail.get_attribute('data-url')
    if link is not None:
        link_thumbnail.append(link)

# 동영상 저장
if not os.path.exists('./mini_project/2_동적 웹 크롤링/videos'):
    os.makedirs('./mini_project/2_동적 웹 크롤링/videos')

for i, link in enumerate(link_thumbnail):
    filename = f'./mini_project/2_동적 웹 크롤링/videos/video{i+1}.mp4'
    urlretrieve(link, filename)

driver.close()