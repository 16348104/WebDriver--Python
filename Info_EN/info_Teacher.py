import re
import os
import time
import random
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, \
    StaleElementReferenceException
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
driver.delete_all_cookies()
print("======Ó¢ÎÄ°æinfo=====")
print('²âÊÔä¯ÀÀÆ÷:' + driver.name)
driver.get('http://101.6.28.150:29009')
driver.maximize_window()
time.sleep(1)


def login(user, password):
    driver.find_element_by_id('user').send_keys(user)
    driver.find_element_by_id('pass').send_keys(password)
    time.sleep(1)
    driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)


login('1992990279', '123')
print('µÇÂ¼Ó¢ÎÄ°æinfo')
time.sleep(5)

driver.find_element_by_xpath("//button[@class='btn btn-default dropdown-toggle']").click()



