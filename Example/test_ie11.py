from selenium import webdriver

driver = webdriver.Ie()  # 调用IE浏览器
# driver = webdriver.Edge()
driver.get('https://www.baidu.com')
print(driver.title)

driver.quit()
