import re
import os
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# driver = webdriver.Safari() #Mac os
print("======进入info=====")
print('测试浏览器:' + driver.name)
driver.get('http://101.6.28.150:29009')
driver.maximize_window()
time.sleep(1)


def login(user, password):
    driver.find_element_by_id('user').send_keys(user)
    driver.find_element_by_id('pass').send_keys(password)
    time.sleep(1)
    driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)


login('1992990279', '123')
time.sleep(5)

driver.find_element_by_xpath("//*[@class='btn btn-default dropdown-toggle']").click()
# 鼠标滑动exit
above = driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[3]/a")
time.sleep(2)
ActionChains(driver).move_to_element(above).perform()
above.click()
# js_logout = "beforeLogout();"
# driver.execute_script(js_logout)
time.sleep(1)
driver.find_element_by_xpath("//*[@class='btn btn-sub']").send_keys(Keys.ENTER)
print('=====退出info=====')
driver.delete_all_cookies()
driver.quit()
