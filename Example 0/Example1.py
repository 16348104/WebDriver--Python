from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)

driver.find_element_by_id('kw').send_keys('selenium')  #在搜索框中输入"selenium"
driver.find_element_by_id('kw').send_keys(Keys.SPACE)  #输入空格键
driver.find_element_by_id('kw').send_keys('python')  #在搜索框中输入"python"
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)  #在搜索框中输入"python"
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')  #输入Control+a模拟全选
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')  #输入Control+c模拟复制
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')  #输入Control+v模拟粘贴
driver.find_element_by_id('kw').send_keys(Keys.ENTER)  #输入回车代替点击搜索按钮

