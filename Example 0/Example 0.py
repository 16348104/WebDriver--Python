from lib2to3.pgen2 import driver

from selenium import webdriver

# browser = webdriver.Chrome()
browser = webdriver.Firefox()
# browser = webdriver.Ie()
browser.get('http://www.baidu.com')
driver.find_element_by_id("kw").send_keys("selenium2")
driver.find_element_by_id("su").click()
