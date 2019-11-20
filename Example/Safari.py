import time


from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Safari()
driver.get('http://info.syx.thcic.cn')
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="userName"]').send_keys("2017013478")
driver.find_element_by_xpath('//input[@name="password"]').send_keys('a123456')
time.sleep(4)
driver.find_element_by_xpath('//td[@class="but"]/input').send_keys(Keys.ENTER)
print("登录信息门户")
time.sleep(5)
driver.find_element_by_xpath('//*[@id="menu"]/li[1]/a[8]').click()
time.sleep(3)
print("进入教学评估")
time.sleep(10)
driver.quit()
