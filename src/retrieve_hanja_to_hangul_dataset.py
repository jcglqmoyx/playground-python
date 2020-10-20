import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
url = "https://hanja.dict.naver.com/"
browser.get(url)
browser.find_element_by_id('autoCompl_Input').send_keys('你')
time.sleep(2)
browser.find_element_by_id('autoCompl_Input').click()
# browser.quit()
