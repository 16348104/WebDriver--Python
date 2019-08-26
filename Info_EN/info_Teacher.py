import re
import os
import time
import random
from public2 import Login_Info
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class LoginTest():
    # 内置方法
    def __int__(self):
        self.driver = webdriver.Chrome()
        # driver = webdriver.Firefox()
        # driver = webdriver.Safari() #Mac os
        self.driver.get('http://infoen.syx.thcic.cn')
        # driver.get('http://101.6.28.150:29009')
        self.driver.maximize_window()
        # driver.set_window_size(1080*760)

    # 教师登录
    def admin_login(self):
        user = '2011990118'
        password = 'a123456'
        Login_Info().user_login(self.driver, user, password)

    # 退出系统
    def test_logout(self):
        Login_Info().user_login(self.driver)

    # 本科生登录
    def test_Bachelor(self):
        user = '2016012872'
        password = 'aihailin4638'
        Login_Info().user_login(self.driver, user, password)

    # 测试enginfo
    def test_enginfo(self):
        print("======进入info=====")
        print('测试浏览器:' + self.driver.name)
        # driver.get('http://101.6.28.150:29009')
        # driver.set_window_size(1080*760)
        print("======Forgot your password======")
        self.driver.find_element_by_xpath('//*[@id="loginForm"]/a').click()
        time.sleep(1)
        # # 切换【第二个窗口】
        windows = self.driver.window_handles
        # # 切换到新窗口
        # driver.switch_to.window(windows[1])
        # window_2 = driver.current_window_handle
        # print('所有句柄:', windows)
        # print("当前窗口：", window_2)
        time.sleep(3)
        # 切换到第1个窗口
        self.driver.switch_to.window(windows[0])
        window_2 = self.driver.current_window_handle
        print("当前窗口：", window_2)

        # def login(user, password):
        #     driver.find_element_by_id('user').send_keys(user)
        #     driver.find_element_by_id('pass').send_keys(password)
        #     time.sleep(1)
        #     driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
        #
        #
        # login('2011990118', 'a123456')
        time.sleep(2)
        print("======Edit Personal Details======")
        self.driver.find_element_by_xpath("//*[@class='btn']").click()
        time.sleep(3)
        # 切换到第1个窗口
        self.driver.switch_to.window(windows[0])
        window_2 = self.driver.current_window_handle
        print("当前窗口：", window_2)
        mk = len(self.driver.find_elements_by_xpath("//ul[@id='tas']/a"))
        i = 0
        while i < mk:
            self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).click()
            time.sleep(1)
            str1 = self.driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).text
            print(str1, "模块")
            i = i + 1
            # driver.find_element_by_xpath('//*[@id="1"]').click()
            hrefs = len(self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a'))
            j = 0
            while j < hrefs:
                str2 = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).text
                # date = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_property('href')
                date = self.driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_attribute('href')
                # time.sleep(1)
                print(str2, ":", date)
                j = j + 1
        self.driver.find_element_by_xpath("//*[@class='btn btn-default dropdown-toggle']").click()
        print("======Change Password======")
        # 鼠标滑动Change Password
        above = self.driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[1]/a")
        time.sleep(2)
        ActionChains(self.driver).move_to_element(above).perform()
        above.click()
        time.sleep(3)

# 执行测试
LoginTest().admin_login()
# LoginTest().test_enginfo()
LoginTest().test_logout()
# print("======进入info=====")
# print('测试浏览器:' + driver.name)
# # driver.get('http://101.6.28.150:29009')
# # driver.set_window_size(1080*760)
# print("======Forgot your password======")
# driver.find_element_by_xpath('//*[@id="loginForm"]/a').click()
# time.sleep(1)
# # # 切换【第二个窗口】
# windows = driver.window_handles
# # # 切换到新窗口
# # driver.switch_to.window(windows[1])
# # window_2 = driver.current_window_handle
# # print('所有句柄:', windows)
# # print("当前窗口：", window_2)
# time.sleep(3)
# # 切换到第1个窗口
# driver.switch_to.window(windows[0])
# window_2 = driver.current_window_handle
# print("当前窗口：", window_2)

# def login(user, password):
#     driver.find_element_by_id('user').send_keys(user)
#     driver.find_element_by_id('pass').send_keys(password)
#     time.sleep(1)
#     driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
#
#
# login('2011990118', 'a123456')
# time.sleep(2)
# print("======Edit Personal Details======")
# driver.find_element_by_xpath("//*[@class='btn']").click()
# time.sleep(3)
# # 切换到第1个窗口
# driver.switch_to.window(windows[0])
# window_2 = driver.current_window_handle
# print("当前窗口：", window_2)
# mk = len(driver.find_elements_by_xpath("//ul[@id='tas']/a"))
# i = 0
# while i < mk:
#     driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).click()
#     time.sleep(1)
#     str1 = driver.find_elements_by_xpath("//ul[@id='tas']/a").pop(i).text
#     print(str1, "模块")
#     i = i + 1
#     # driver.find_element_by_xpath('//*[@id="1"]').click()
#     hrefs = len(driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a'))
#     j = 0
#     while j < hrefs:
#         str2 = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).text
#         # date = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_property('href')
#         date = driver.find_elements_by_xpath('//*[@id="fir_ul"]/li/a').pop(j).get_attribute('href')
#         # time.sleep(1)
#         print(str2, ":", date)
#         j = j + 1
# driver.find_element_by_xpath("//*[@class='btn btn-default dropdown-toggle']").click()
# print("======Change Password======")
# # 鼠标滑动Change Password
# above = driver.find_element_by_xpath("//ul[@class='dropdown-menu']/li[1]/a")
# time.sleep(2)
# ActionChains(driver).move_to_element(above).perform()
# above.click()
# time.sleep(3)

# # js退出
# js_logout = "beforeLogout();"
# driver.execute_script(js_logout)
# time.sleep(1)
# driver.find_element_by_xpath("//*[@class='btn btn-sub']").send_keys(Keys.ENTER)
# print('=====退出info=====')
# driver.delete_all_cookies()
# driver.quit()
