# coding=utf-8
import random

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Firefox()
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(
#     executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/geckodriver')# mac  firefox
print("======登录阿里云监控=====")
print('测试浏览器:' + driver.name)
driver.get('https://cloudmonitor.console.aliyun.com')
driver.maximize_window()
driver.implicitly_wait(1)
driver.switch_to.frame('alibaba-login-box')  # 切入框架
driver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
# driver.find_element_by_xpath('//input[@id="fm-login-id"]').send_keys('')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('')
# driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').send_keys(
#     Keys.ENTER)
date = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/div[2]/p').text
print(date)
time.sleep(20)
driver.switch_to.default_content()
time.sleep(2)
driver.find_element_by_css_selector(
    'body > div.viewframeContainer > div > div.aliyun-console-help-guide > div.help-guide-step.help-guide-step-1 > div.help-guide-step-header > i.topbar-sidebar-no').click()
time.sleep(2)
print('站点监控')
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.2020520111.aliyun_sidebar.aliyun_sidebar_cms.6ff9d103iaAGn8#/home/ecs')
time.sleep(3)
print('站点管理')
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.12818093.aliyun_sidebar.aliyun_sidebar_cms.488716d0VtQA3i#/newSite/list/')
time.sleep(3)
driver.find_element_by_xpath("//span[contains(text(),'网络学堂应用服务监控2')]").click()
time.sleep(10)
print('截图')
# driver.save_screenshot('/Users/xdx/Desktop/Monitor.png')  # mac
driver.save_screenshot('C:/Users/zb/Downloads/FireShot/Monitor.png')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))
print('在', current_time, '退出cloudmonitor')
driver.close()
