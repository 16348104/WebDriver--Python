from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# browser = webdriver.Chrome(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  #mac os
browser.get('http://learn.tsinghua.edu.cn')
elem_user = browser.find_element_by_name('i_user')
elem_pass = browser.find_element_by_name('i_pass')
# 清空输入
elem_user.clear()
elem_pass.clear()
# 键入用户名
# elem_user.find_element_by_name('i_user').send_keys('2016012872')
# 键入密码
elem_pass.find_element_by_name('i_pass').send_keys('')
browser.find_element_by_id('loginButtonId').click()
time.sleep(10)
# 取ID为txtPwd的网页元素(密码输入元素)
# elem_pass=driver.find_element_by_id('txtPwd')
# #清空输入
# elem_pass.clear()
#
# elem_pass.send_keys('*****')
# #取ID为btnLogin的登录按钮
# elem_login=driver.find_element_by_id('btnLogin')
# #点击登录按钮
# elem_login.click()
# browser.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# browser.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')
# browser.find_element_by_class_name()
browser.quit()
