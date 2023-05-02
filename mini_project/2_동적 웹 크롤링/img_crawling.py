from selenium import webdriver as wb
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
import time 
import os

# 고양이 이미지 페이지를 driver 객체로 생성
driver = wb.Chrome() 
driver.get('https://search.naver.com/search.naver?where=image&sm=tab_jum&query=%EA%B3%A0%EC%96%91%EC%9D%B4')
time.sleep(2)

# 이미지 태그 접근
img = driver.find_elements(By.CSS_SELECTOR, '._image._listImage')
# 이미지 태그의 src속성값 수집
src = [i.get_attribute('src') for i in img]

# src_lst에 src의 data:image가 있는 문자열을 뺀 데이터만 담기
src_list = []
for i in src :
    if 'data:image' not in i :
        src_list.append(i)

if not os.path.exists('SW분야 벤처스타트업 아카데미/mini_project/2_동적 웹 크롤링/img'):
    os.makedirs('SW분야 벤처스타트업 아카데미/mini_project/2_동적 웹 크롤링/img')

for i in range(10) : # .jpg 이미지 파일로 10장 저장
    urlretrieve(src_list[i], f'SW분야 벤처스타트업 아카데미/mini_project/2_동적 웹 크롤링/img/cat_{i+1}.jpg')
driver.close() # 브라우저 닫기