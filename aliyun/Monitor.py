# coding=utf-8
from selenium import webdriver
import time

driver = webdriver.Firefox(executable_path='C:/Users/zb/Desktop/test/python/geckodriver.exe')
# driver = webdriver.Chrome()
# driver = webdriver.Chrome(
#     executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/geckodriver')# mac  firefox
print("======登录阿里云监控=====")
print('测试浏览器:' + driver.name)
driver.get(
    'https://account.aliyun.com/login/login.htm?oauth_callback=https%3A%2F%2Fhome.console.aliyun.com%2F%3Fspm%3D5176.8142029.388261.3.e9396d3eVocMar')
driver.maximize_window()
driver.implicitly_wait(1)
driver.switch_to.frame('alibaba-login-box')  # 切入框架
driver.find_element_by_xpath('//*[@id="login"]/div[1]/i').click()
# driver.find_element_by_xpath('//input[@id="fm-login-id"]').send_keys('2019xdx')
# time.sleep(1)
# driver.find_element_by_xpath('//*[@id="fm-login-password"]').send_keys('ustb55aliyun')
# driver.find_element_by_xpath('//*[@id="login-form"]/div[4]/button').send_keys(
#     Keys.ENTER)
date = driver.find_element_by_xpath('//*[@id="login"]/div[2]/div/div[1]/div[2]/p').text
print(date)
time.sleep(20)
driver.switch_to.default_content()
driver.find_element_by_css_selector(
    '#console-base > div > div.aliyun-console-help-guide > div.help-guide-step.help-guide-step-1 > div.help-guide-step-header > i.topbar-sidebar-no').click()
time.sleep(2)
# driver.find_element_by_xpath('//*[@id="consoleBaseTopbarRoot"]/div[1]').click()
# driver.get('https://cloudmonitor.console.aliyun.com')
# 站点监控
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.2020520111.aliyun_sidebar.aliyun_sidebar_cms.6ff9d103iaAGn8#/home/ecs')
time.sleep(2)
# 站点管理
driver.get(
    'https://cloudmonitor.console.aliyun.com/?spm=5176.12818093.aliyun_sidebar.aliyun_sidebar_cms.488716d0VtQA3i#/newSite/list/')
time.sleep(2)
driver.find_element_by_xpath("//span[contains(text(),'网络学堂应用服务监控2')]").click()
# 截图
# driver.save_screenshot('/Users/xdx/Desktop/Monitor.png')  # mac
driver.save_screenshot('C:/Users/zb/Downloads/FireShot/Monitor.png')
time.sleep(3)
driver.close()
