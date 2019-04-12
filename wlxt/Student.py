from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# driver = webdriver.Chrome(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  #mac os
# driver = webdriver.Safari() #Mac os
driver.get('http://learn.tsinghua.edu.cn')
driver.maximize_window()
# 登录网络学堂
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
time.sleep(40)  # 休眠40秒
driver.find_element_by_id('loginButtonId').click()

driver.get(
    'http://learn.tsinghua.edu.cn/f/wlxt/index/course/student/course?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')
time.sleep(1)
# # 浏览公告#
# driver.get(
#     'http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/student/beforePageListXs?wlkcid=2018-2019-226ef84e7689589e901689906e324686a&sfgk=0')
# driver.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# time.sleep(1)
# driver.find_element_by_id('backBtn').click()

# 课程邮件#
driver.get(
    'http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/student/beforePageList?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')
# driver.find_element_by_xpath(".//*[@id='list']/tbody/tr[1]/td[2]/a").click()
# time.sleep(1)
# driver.find_element_by_id('returnButton').click()
driver.find_element_by_xpath("//*[@id='content']/div[2]/div[1]/div/span[2]/a").click()
driver.find_elements_by_xpath("//*[@id='myTags']")
addresses = driver.find_elements_by_xpath("//*[@id='myTags']/li/a/span")   #需要正则表达式
for addresses in addresses:
    addresses.click()
# driver.find_element_by_name('i_user').send_keys('')
time.sleep(5)

driver.quit()


# driver.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# driver.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')
