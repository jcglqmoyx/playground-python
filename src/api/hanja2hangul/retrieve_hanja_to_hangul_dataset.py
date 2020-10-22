import time

from selenium import webdriver

url = "https://hanja.dict.naver.com/"
hanja_input_id = 'autoCompl_Input'
hangul_output_class = 'kor_tone'

chinese_characters_file = open(
    '/home/jcglqmoyx/projects/pycharm-projects/playground-python/src/api/hanja2hangul/chinese.txt', 'r')
chinese_characters = chinese_characters_file.read()
chinese_characters_file.close()
result_file = open('result.txt', 'a')

for chinese_character in chinese_characters:
    try:
        chrome_options = webdriver.ChromeOptions()
        browser = webdriver.Chrome()
        browser.get(url)
        input_box = browser.find_element_by_id(hanja_input_id)
        input_box.send_keys(chinese_character)
        time.sleep(1)
        browser.find_element_by_id(hanja_input_id).click()
        time.sleep(1)
        korean = browser.find_element_by_class_name(hangul_output_class).text[-1]
        print(chinese_character,korean, '..........')
        result_file.write(chinese_character + ' ' + korean + '\n')
        # input_box.clear()
        browser.quit()
        time.sleep(1)
    except Exception:
        print('..')

result_file.close()
