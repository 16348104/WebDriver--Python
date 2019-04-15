from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os
print("========登录网络学堂==========")
driver.get('http://learn.tsinghua.edu.cn')
driver.maximize_window()
# 登录网络学堂，【第一个窗口】
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
driver.find_element_by_name('i_user').send_keys('2016012872')  # 键入用户名
driver.find_element_by_name('i_pass').send_keys('aihailin0928')  # 键入密码
driver.find_element_by_id('loginButtonId').click()
# 进入课程【第二个窗口】
# driver.find_element('//*[@id="suoxuecourse"]/dd/div[2]/div[1]/a')
driver.find_element_by_link_text('基于Linux的C++(20740084-998)').click()
time.sleep(3)  # 休眠
# 使用第二种方法切换浏览器【切换到第二个窗口】
window_1 = driver.current_window_handle
windows = driver.window_handles
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
# driver.get( 'http://learn.tsinghua.edu.cn/f/wlxt/index/course/student/course?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')

print("===========测试课程公告============")
# # 浏览公告#
# driver.get(
#     'http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/student/beforePageListXs?wlkcid=2018-2019-226ef84e7689589e901689906e324686a&sfgk=0')
# driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# time.sleep(1)
# driver.find_element_by_id('backBtn').click()

# 课程邮件#
print('======测试课程邮件=====')
driver.find_element_by_link_text('课程邮件').click()
# driver.get( "http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/student/beforePageList?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()
time.sleep(3)
driver.find_element_by_id('returnButton').click()
driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()
addresses = driver.find_elements_by_xpath("//span[contains(@class,'text-icon')]")
for i in addresses:
    # if i.get_attribute('text') != '肖大兴':
    i.click()
    time.sleep(1)
driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys('wlxt@tsinghua.edu.cn')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]/input').send_keys('xiesup@tsinghua.edu.cn')
driver.implicitly_wait(3)
driver.find_element_by_xpath('//input[@id="bt"]').send_keys('网络学堂学生端测试邮件！')
driver.find_element_by_xpath('//input[@id="submitButton"]').click()
time.sleep(3)
driver.quit()

# print(len(addresses))


# for add in addresses:
#     add.click()
# driver.find_element_by_name('i_user').send_keys('')
# time.sleep(20)


# driver.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# driver.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')
