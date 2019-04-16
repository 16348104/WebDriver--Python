from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os
print("======登录网络学堂=====")
driver.get('http://learn.tsinghua.edu.cn')
driver.maximize_window()
# 登录网络学堂，【第一个窗口】
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
driver.find_element_by_name('i_user').send_keys('2016012872')  # 键入用户名
driver.find_element_by_name('i_pass').send_keys('aihailin0928')  # 键入密码
driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
# 进入课程【第二个窗口】
# driver.find_element('//*[@id="suoxuecourse"]/dd[5]/div[2]/div[1]/a').click()
# driver.find_element_by_link_text('基于Linux的C++(20740084-998)').click()
driver.find_element_by_xpath('//*[@id="suoxuecourse"]//a[contains(text(),"基于Linux的C++(20740084-998)")]').click()
time.sleep(2)  # 休眠
# 使用第二种方法切换浏览器【切换到第二个窗口】
window_1 = driver.current_window_handle
windows = driver.window_handles
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(2)
print('=====登录成功=====')

# print("=====测试课程公告=====")
# driver.find_element_by_link_text('课程公告').click()
# driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# time.sleep(1)
# driver.find_element_by_id('backBtn').click()
# print('=====公告测试完毕=====')

# 课程邮件#
# print('=====测试课程邮件=====')
# driver.find_element_by_link_text('课程邮件').click()
# driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()
# time.sleep(3)
# driver.find_element_by_id('returnButton').click()
# driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()
# addresses = driver.find_elements_by_xpath("//span[contains(@class,'text-icon')]")
# for i in addresses:
#     # if i.get_attribute('text') != '肖大兴':
#     i.click()
#     time.sleep(1)
# driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys('wlxt@tsinghua.edu.cn')
# driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys(Keys.ENTER)
# driver.implicitly_wait(3)
# # driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]/input').send_keys('xiesup@tsinghua.edu.cn')
# # driver.implicitly_wait(3)
# driver.find_element_by_xpath('//input[@id="bt"]').send_keys('网络学堂学生端测试邮件！')
# driver.find_element_by_xpath('//input[@id="submitButton"]').click()
# time.sleep(3)
# print('=====邮件测试完毕=====')


#课程文件
print("=====测试课程文件=====")
driver.find_element_by_link_text('课程文件').click()
li = driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]")
print(len(li))
print('=====课件测试完毕=====')

# print('=====测试课程作业=====')
# driver.find_element_by_link_text('课程作业').click()
# driver.find_element_by_xpath('//*[@id="wtj"]/tbody/tr[1]/td[2]/a').click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//input[@id="saveBtn"]').click()
# driver.implicitly_wait(2)
# driver.find_element_by_xpath('//*[@id="s_documention"]')
# driver.find_element_by_id('fileupload').send_keys(r'D:/listening.pdf')  # 上传文件
# driver.find_element_by_xpath("//input[@onclick='daijiao()']").click()
# driver.implicitly_wait(5)
# print('=====作业测试完毕=====')
# driver.quit()

# print(len(addresses))




# driver.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# driver.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')
