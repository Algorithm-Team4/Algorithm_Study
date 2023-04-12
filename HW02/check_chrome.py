from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service('/path/to/chromedriver')
driver = webdriver.Chrome(service=service)

browser_version = driver.capabilities['browserVersion']
print(browser_version)