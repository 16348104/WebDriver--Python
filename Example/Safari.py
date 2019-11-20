import time


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

browser = webdriver.Safari()
browser.get('http://weibo.com')
browser.maximize_window()
time.sleep(10)



# 不记住
browser.find_element_by_xpath("//input[@id='login_form_savestate']").click()
time.sleep(3)
# 输入帐号密码
# browser.find_element_by_xpath("//input[@id='loginname']").send_keys('dxx2018@sina.cn')
# browser.find_element_by_xpath("//input[@type='password']").send_keys('2008@sina')
# time.sleep(4)
# 点击登录
# browser.find_element_by_xpath("//div[@id='pl_unlogin_home_login']//div[6]//a[1]").click()
time.sleep(15)
browser.quit()
# 查找页面中的所有 点赞按钮
# allzan = browser.find_elements_by_css_selector('em.W_ficon.ficon_praised.S_txt2')
#
# time.sleep(10)
# browser.quit()
