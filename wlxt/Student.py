from selenium import webdriver
import time

browser = webdriver.Chrome()
# browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser = webdriver.Firefox(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/geckodriver')  #mac firefox
# browser = webdriver.Chrome(executable_path = '/Users/xiaodaxing/Downloads/PycharmProjects/Example 0/chromedriver')  #mac os
# browser = webdriver.safari()
browser.get('http://learn.tsinghua.edu.cn')
time.sleep(40)#休眠40秒
# browser.find_element_by_name('i_user').clear()
# browser.find_element_by_name('i_pass').clear()
# # 键入用户名
# browser.find_element_by_name('i_user').send_keys('2016012872')
# # 键入密码
# browser.find_element_by_name('i_pass').send_keys('aihailin0928')
# browser.find_element_by_id('loginButtonId').click()

browser.get('http://learn.tsinghua.edu.cn/f/wlxt/index/course/student/course?wlkcid=2018-2019-226ef84e7689589e901689906e324686a')
time.sleep(1)
browser.get('http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/student/beforePageListXs?wlkcid=2018-2019-226ef84e7689589e901689906e324686a&sfgk=0')
browser.find_element_by_link_text('new').click()
browser.find_element_by_id('wjmc').click()
time.sleep(5)


# browser.get(r'E:\163study\WebDriver--Python\upload.html')  # 文件的地址
# browser.find_element_by_name('file').send_keys(r'E:/map.png')  # 上传文件
# print('文件上传完毕')

# browser.quit()
