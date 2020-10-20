import time

from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
browser = webdriver.Chrome()
url = "https://hanja.dict.naver.com/"
browser.get(url)
hanja_input_id = 'autoCompl_Input'
hangul_output_class = 'kor_tone'
browser.find_element_by_id(hanja_input_id).send_keys('你')
time.sleep(2)
browser.find_element_by_id(hanja_input_id).click()
res = browser.find_elements_by_class_name(hangul_output_class)[0].value
print(res)
# browser.quit()
