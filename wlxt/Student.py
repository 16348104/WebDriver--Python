#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os
print("======登录网络学堂=====")
print('测试浏览器:' + driver.name)
driver.get('http://learn.tsinghua.edu.cn')
driver.maximize_window()
# 登录网络学堂，【第一个窗口】
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
# time.sleep(30)
driver.find_element_by_name('i_user').send_keys('')  # 键入用户名
driver.find_element_by_name('i_pass').send_keys('')  # 键入密码
driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
# 进入课程【第二个窗口】
# driver.find_element('//*[@id="suoxuecourse"]/dd[5]/div[2]/div[1]/a').click()
# driver.find_element_by_link_text('基于Linux的C++(20740084-998)').click()
driver.find_element_by_xpath('//*[@id="suoxuecourse"]//a[contains(text(),"20740084-998")]').click()
time.sleep(1)  # 休眠
print(driver.title)
print(driver.current_window_handle)
# 【切换到第二个窗口】
window_1 = driver.current_window_handle  # 当前窗口句柄
windows = driver.window_handles  # 窗口总数
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
print(window_1)
print(current_window)
print('=====登录成功=====')

print("=====测试课程公告=====")
driver.find_element_by_link_text('课程公告').click()
driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[1]/a")
driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# if driver.find_element_by_xpath("//div[@id='ggfj']").is_enabled():
#     fj = driver.find_element_by_xpath("//div[@id='ggfj']").is_enabled()
#     print('公告附件:'+fj)
#     # fj = driver.find_element_by_xpath("//div[@id='ggfj']//a[@id='wjid']")
#
# else:
#     print('公告附件无')
# driver.find_element_by_id('backBtn').click()

# def is_element_exist(id):
#     s = driver.find_element_by_id(id=wjid)
#     if len(s) == 0:
#         print
#         "元素未找到:%s" % id
#         return False
#     elif len(s) == 1:
#         return True
#     else:
#         print
#         "找到%s个元素：%s" % (len(s), id)
#         return False
#
#
# if is_element_exist("#wjid"):
#     driver.find_element_by_id("wjid").click()  # 浏览公告附件

# print('=====公告测试完毕=====')

# 课程邮件#
# print('=====测试课程邮件=====')
# driver.find_element_by_link_text('课程邮件').click()
# driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()  # 浏览邮件
# driver.implicitly_wait(2)
# driver.find_element_by_id('returnButton').click()
# driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()
# addresses = driver.find_elements_by_xpath("//span[contains(@class,'text-icon')]")
# for i in addresses:
#     # if i.get_attribute('text') != '肖大兴':
#     i.click()
#     time.sleep(1)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys('wlxt@tsinghua.edu.cn')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys(Keys.ENTER)
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]/input').send_keys('xiesup@tsinghua.edu.cn')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]//input').send_keys(Keys.ENTER)
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]/input').send_keys('yumj@tsinghua.edu.cn')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]//input').send_keys(Keys.ENTER)
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//input[@id="bt"]').send_keys('网络学堂学生端测试邮件！')
# # driver.find_element_by_xpath("//textarea[@id='nrStr']")
# # js = "document.getElementById('nrStr').value = new Date().toLocaleDateString();"
# # val = driver.execute_script(js)
# iframe = driver.find_element_by_xpath("//iframe[contains(@title,'nrStr')]")
# driver.switch_to.frame(iframe)
# driver.find_element_by_xpath("//body[starts-with(@class,'cke')]").send_keys('学生端测试邮件')
# driver.switch_to.default_content()
# # driver.find_element_by_xpath('//input[@id="submitButton"]').click()
# driver.implicitly_wait(4)
# print('=====邮件测试完毕=====')

# 课程文件
# print("=====测试课程文件=====")
# driver.find_element_by_link_text('课程文件').click()
# li = driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]")
# ran = random.randint(1, 10) - 1  # 随机数
# print(ran)
# li.pop(ran).click()
# # if driver.find_element_by_xpath("//img[@src='/res/app/wlxt/img/pbtn.png']"):
# #     print("文本")
# # if driver.find_element_by_xpath("audio[@id='mp3']").is_enabled():
# #     print("mp3")
# # if driver.find_element_by_xpath("//button[@title='Play Video']").is_enabled():
# #     print("mp4")
# driver.implicitly_wait(3)
# print('=====课件测试完毕=====')

# print('=====测试课程作业=====')
# driver.find_element_by_link_text('课程作业').click()
# driver.find_element_by_xpath('//*[@id="wtj"]/tbody/tr[1]/td[2]/a').click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//input[@id="saveBtn"]').click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//textarea[@id="s_documention"]')
# js = "document.getElementById('s_documention').value= new Date().toLocaleDateString()"
# driver.execute_script(js)
# driver.find_element_by_id('fileupload').send_keys(r'D:/listening.pdf')  # 上传文件
# # driver.find_element_by_xpath("//input[@onclick='daijiao()']").click()
# driver.implicitly_wait(5)
# print('=====作业测试完毕=====')

# driver.quit()

# print(len(addresses))


# driver.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# driver.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# driver.find_element_by_name('file').send_keys(r'/Users/xiaodaxing/Downloads/bear.jpg')  # mac上传文件
# print('文件上传完毕')
