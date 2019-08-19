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
# driver.get('http://101.6.28.150:29009')
driver.get('http://infoen.syx.thcic.cn')

driver.maximize_window()
time.sleep(1)


def login(user, password):
    driver.find_element_by_id('user').send_keys(user)
    driver.find_element_by_id('pass').send_keys(password)
    time.sleep(1)
    driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)


login('2019430117', 'a123456')
time.sleep(1)
mk = len(driver.find_elements_by_xpath("//ul[@id='tas']/a"))
i = 0
while i < mk:
    driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).click()
    time.sleep(1)
    str1 = driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).text
    print(str1, "模块")
    i = i + 1
    # driver.find_element_by_xpath('//*[@id="1"]').click()
    hrefs = len(driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a'))
    j = 0
    while j < hrefs:
        str2 = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).text
        date = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_attribute('href')
        # time.sleep(1)
        print(str2, ":", date)
        j = j + 1
driver.find_element_by_xpath("//*[@class='btn btn-default dropdown-toggle']").click()
# # 鼠标滑动exit
# above = driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[3]/a")
# time.sleep(2)
# ActionChains(driver).move_to_element(above).perform()
# above.click()

# js退出
js_logout = "beforeLogout();"
driver.execute_script(js_logout)
time.sleep(1)
driver.find_element_by_xpath("//*[@class='btn btn-sub']").send_keys(Keys.ENTER)
print('=====退出info=====')
driver.delete_all_cookies()
driver.quit()
