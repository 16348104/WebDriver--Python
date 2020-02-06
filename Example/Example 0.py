from selenium import webdriver
import time

# browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# browser = webdriver.Chrome(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  #mac os
# browser = webdriver.Safari()  # Mac safari
# browser.maximize_window()
# browser.get('http://www.baidu.com')
# browser.find_element_by_name('i_user').clear()
# browser.find_element_by_name('i_pass').clear()
# 键入用户名
# browser.find_element_by_name('i_user').send_keys('')
# # 键入密码
# browser.find_element_by_name('i_pass').send_keys('')
# browser.find_element_by_id('loginButtonId').click()
# time.sleep(2)
# browser.get('http://learn.tsinghua.edu.cn/f/wlxt/index/course/student/course?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')

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
# browser.quit()
# ==============

# 打开课工场网站主页【第一个窗口】
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
driver.get('http://www.baidu.cn/')
driver.maximize_window()
# 点击热点关注，进入【第二个窗口】
# driver.find_element_by_link_text('热点关注').click()
time.sleep(5)
# =========================================
# 使用第一种方法切换浏览器【切换到第二个窗口】
# windows = driver.window_handles
# driver.switch_to.window(windows[-1])
# time.sleep(3)
#==========================================
# 使用第二种方法切换浏览器【切换到第二个窗口】
# window_1 = driver.current_window_handle
# windows = driver.window_handles
# for current_window in windows:
#     if current_window != window_1:
#         driver.switch_to.window(current_window)
# time.sleep(3)
# 点击课程库中的某个课程，进入课程详情界面【在第二个窗口页面进行元素点击操作，来判断窗口是否切换成功】
driver.find_element_by_xpath('//*[@id="python"]/div[2]/a').click()
time.sleep(3)
# 关闭浏览器
driver.quit()
print('测试通过')
