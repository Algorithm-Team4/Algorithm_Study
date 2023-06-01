from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import datetime
import pandas as pd
import re

option = Options()
user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
#브라우저 꺼짐 방지
option.add_experimental_option("detach",True)
#user-agent 추가이유 -> bot이 아니라는걸 알림 
option.add_argument('user-agent=' + user_agent)
#크롬 드라이버 자동 설치
try:
    s = Service(ChromeDriverManager().install())
    browser = webdriver.Chrome(service=s, options=option)
except Exception as e:
    print(e)
# 스팀 사이트 접속
browser.get('https://store.steampowered.com/')

# 신규 및 특집 클릭 -> 최고 인기 제품 클릭
browser.find_element(by=By.XPATH, value='//*[@id="noteworthy_tab"]/span/a[1]').click()
browser.find_element(by=By.XPATH, value='//*[@id="noteworthy_flyout"]/div/a[2]').click()
time.sleep(5)
# 1위 게임 클릭
browser.find_element(by=By.XPATH, value='//*[@id="application_root"]/div/div/div/div/div[3]/table/tbody/tr[1]/td[3]/a/div').click()

# 스크롤다운 함수
def doScrollDown(whileSeconds):
        start = datetime.datetime.now()
        end = start + datetime.timedelta(seconds=whileSeconds)
        while True:
            browser.execute_script('window.scrollTo(0, document.body.scrollHeight);')
            time.sleep(1)
            if datetime.datetime.now() > end:
                break

# 모든 리뷰 보기를 클릭 하기 위해 스크롤 다운
doScrollDown(3)
# 모든 리류 보기 클릭
browser.find_element(by=By.XPATH, value = '//*[@id="ViewAllReviewssummary"]/a').click()

# 한국어로 변경
browser.find_element(by=By.XPATH, value = '//*[@id="filterlanguage_activeday"]').click()
browser.find_element(by=By.XPATH, value = '//*[@id="filterlanguage_option_5"]').click()

# 100초 동안 스크롤한 리뷰 크롤링
doScrollDown(100)
text_elements= browser.find_elements(by=By.CSS_SELECTOR, value = '.apphub_CardTextContent')
img_elements=browser.find_elements(by = By.CSS_SELECTOR, value = '.thumb')

table = []

for i in range(0, len(text_elements)):
    text = text_elements[i].text
    # 날짜 추출
    date_match_1 = re.search(r"Posted: (\d{1,2}\s\w+,\s\d{4})", text)
    date_match_2 = re.search(r"Posted: (\w+\s\d{1,2},\s\d{4})", text)
    
    if date_match_1:
        date = date_match_1.group(1)
        text = text.replace("Posted: {}".format(date), '')
    elif date_match_2:
        date = date_match_2.group(1)
        text = text.replace("Posted: {}".format(date), '')
    else:
        date = None
    # 얼리 엑세스 리뷰 여부 확인
    early_access_match = re.search(r"EARLY ACCESS REVIEW", text)
    if early_access_match:
        early_access_review = 1
        text = text.replace("EARLY ACCESS REVIEW", '')
    else:
        early_access_review = 0

    el = img_elements[i].find_element(by=By.TAG_NAME, value='img')
    src = el.get_attribute('src')

    if 'thumbsUp' in src:
        src = 1  # 추천
    else:
        src = 0  # 비추천

    table.append([text, date, early_access_review, src])


df = pd.DataFrame(table, columns = ['리뷰','날짜','early_access 유무', 'src(1= 추천, 0 = 비추천)'])
df.to_csv('gamereviews.csv', encoding = 'utf-8-sig')