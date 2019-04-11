from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# browser = webdriver.Chrome(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  #mac os
# browser = webdriver.safari()#Mac os
browser.get('http://learn.tsinghua.edu.cn')
browser.maximize_window()
# 登录网络学堂
browser.find_element_by_name('i_user').clear()
browser.find_element_by_name('i_pass').clear()
time.sleep(40)  # 休眠40秒
browser.find_element_by_id('loginButtonId').click()

browser.get(
    'http://learn.tsinghua.edu.cn/f/wlxt/index/course/student/course?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')
time.sleep(1)
# # 浏览公告#
# browser.get(
#     'http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/student/beforePageListXs?wlkcid=2018-2019-226ef84e7689589e901689906e324686a&sfgk=0')
# browser.find_element_by_xpath(".//*[@id='table']/tbody/tr[1]/td[1]/a").click()
# time.sleep(1)
# browser.find_element_by_id('backBtn').click()

# 课程邮件#
browser.get(
    'http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/student/beforePageList?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')
browser.find_element_by_xpath(".//*[@id='list']/tbody/tr[1]/td[2]/a").click()
time.sleep(1)
browser.find_element_by_id('returnButton').click()
browser.find_element_by_class_name('btn').click()
time.sleep(1)

browser.quit()


# browser.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# browser.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')
