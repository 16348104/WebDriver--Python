import time
from selenium import webdriver
class LoginJXGL():
    # 登录
    def userlogin(self, driver, user, password):
        driver.find_element_by_xpath('//*[@id="userName').send_keys('user')
        driver.find_element_by_id('pass').send_keys('password')

