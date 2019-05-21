from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# driver = webdriver.Safari()  # Mac os
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  # mac  chrome
driver = webdriver.Chrome()
driver.get("http://www.baidu.com")
time.sleep(3)
data = driver.find_element_by_id("cp").text
print(data)  # 打印信息
print(driver.find_element_by_id('kw').get_property('maxlength'))
print(driver.find_element_by_id('kw').get_attribute('autocomplete'))
driver.find_element_by_id('kw').send_keys('selenium')  # 在搜索框中输入"selenium"
driver.find_element_by_id('kw').send_keys(Keys.SPACE)  # 输入空格键
driver.find_element_by_id('kw').send_keys('python')  # 在搜索框中输入"python"
driver.find_element_by_id('kw').send_keys(Keys.BACKSPACE)  # 在搜索框中输入"python"
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'a')  #输入Control+a模拟全选
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'c')  #输入Control+c模拟复制
# driver.find_element_by_id('kw').send_keys(Keys.CONTROL, 'v')  #输入Control+v模拟粘贴
driver.find_element_by_id('kw').send_keys(Keys.ENTER)  # 输入回车代替点击搜索按钮

# driver.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# driver.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# driver.find_element_by_name('file').send_keys(r'/Users/xiaodaxing/Downloads/bear.jpg')  # mac上传文件
# print('文件上传完毕')

js = "alert('这是一个测试Alert弹窗')"
driver.execute_script(js)
time.sleep(2)
t = driver.switch_to.alert.text  # 返回alert中文字信息
print(t)
time.sleep(2)
# driver.switch_to_alert().accept()  # 点击弹出里面的确定按钮
# driver.switch_to_alert().dismiss() # 点击弹出上面的X按钮


time.sleep(3)
driver.quit()
