# coding=utf-8
from selenium import webdriver

driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/geckodriver')
print("======登录阿里云监控=====")
print('测试浏览器:' + driver.name)
driver.get('https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fhome.console.aliyun.com%2F%3Fspm%3D5176.8142029.388261.3.e9396d3eVocMar')
driver.maximize_window()
driver.implicitly_wait(1)
driver.find_element_by_xpath('//*[@id="fm-login-id"]')
driver.close()
