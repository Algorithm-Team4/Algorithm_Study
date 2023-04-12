from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
from selenium.webdriver.common.by import By

query = input("검색어를 입력하세요: ")

# 크롬드라이버 로드
driver = webdriver.Chrome("/path/to/chromedriver") # 본인의 chromedriver 경로를 입력해주세요.

# 구글 검색 페이지로 이동
driver.get("https://www.google.com")

# 검색어 입력
search_box = driver.find_elements(By.NAME, "q")
search_box.send_keys(query)
search_box.send_keys(Keys.RETURN)

# 검색 결과 파싱
search_results = driver.find_elements_by_css_selector("div.g")

# 검색 결과 출력
for result in search_results:
    title = result.find_element_by_css_selector("h3").text
    link = result.find_element_by_css_selector("a").get_attribute("href")
    description = result.find_element_by_css_selector("span.aCOpRe").text
    print(f"{title}\n{link}\n{description}\n")
    
# 크롬드라이버 종료
driver.quit()