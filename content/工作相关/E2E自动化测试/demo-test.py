# -*- coding:utf-8 -*-
# @UpdateTime : 2020/4/17 12:09 下午

from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By

from pageObject.config.page_url_config import TEST_SERVER_ROOT_URL
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC  # 判断元素是否被定位到

wd = webdriver.Chrome()
# wd.get("https://www.baidu.com")  # 打开百度浏览器
# wd.find_element_by_id("kw").send_keys("selenium")  # 定位输入框并输入关键字
# wd.find_element_by_id("su").click()  # 点击[百度一下]搜索
# time.sleep(3)  # 等待3秒
# wd.quit()   #关闭浏览器


wd.get(TEST_SERVER_ROOT_URL + "teacher/list")
time.sleep(1)
# print(type(wd.find_element(By.XPATH,
#                            '//*[@id="app"]/div/section/section/main/div[2]/div/div/div/div[2]/div[3]/table/tbody/tr[1]/td[2]/div').text))
global el
try:
    WebDriverWait(wd, 20).until(
        EC.visibility_of_element_located((By.XPATH, '//*[@id="app"]/div/section/section/main/div[2]/div/form/div[3]/div/button')))  # 这个位置的元素是否有宽和高，具体可以看下方法描述，讲的很清晰
    el = wd.find_element(*(By.CSS_SELECTOR, '#app > div > section > section > main > div.monitor > div > form > div:nth-child(3) > div > button'))
except Exception as errorMessage:
    print(u"元素定位在页面中无法找x到！" + " exception: " + errorMessage.message)
el.send_keys(Keys.ENTER)
time.sleep(3)
# wd.find_element(By.CLASS_NAME, "el-input__inner").send_keys('asdfaf')
# time.sleep(3)
# wd.find_element_by_css_selector("[class='el-button el-button--success el-button--mini']").click()


# chrome_options = webdriver.ChromeOptions()
# chrome_options.add_argument("--headless")
# wd = webdriver.Chrome(chrome_options=chrome_options)
# wd = webdriver.Chrome()
# wd.get(TEST_SERVER_ROOT_URL + 'teacher/form')
# time.sleep(1)
# input_list = wd.find_elements(By.CSS_SELECTOR, "input[class='el-input__inner']")
# print(input_list)
# for el in input_list:
#     el.send_keys(u"you are 小猪猪")
# wd.find_element(By.XPATH,
#                 '//*[@id="app"]/div/section/section/main/div[2]/div/div/form/div[9]/div/button[1]').click()
# wd.get(TEST_SERVER_ROOT_URL + "teacher/list")
# time.sleep(1)
wd.close()
