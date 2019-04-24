# coding=utf-8
from selenium import webdriver
import time

from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:/Users/zb/Desktop/test/python/chromedriver.exe')  # 定时任务
# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# driver = webdriver.Firefox(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os

######################################################登录网络学堂######################################################
# 打开网络学堂
driver.get("http://learn.tsinghua.edu.cn")
driver.maximize_window()
print("======登录网络学堂=====")
print('测试浏览器:' + driver.name)
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 计算明天时间
tomorrow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 3600))
print("当前时间戳为:", ticks)
# print ("当前时间戳为:", tomorrow)

driver.find_element_by_name("i_user").send_keys("")
driver.find_element_by_name("i_pass").send_keys("")
driver.find_element_by_id("loginButtonId").click()
# 打开公告
print('测试课程公告')
time.sleep(1)
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# 发布公告
time.sleep(2)
driver.find_element_by_name("bt").send_keys("测试公告" + ticks)
driver.find_element_by_xpath("//div[@class='list title notext']//label[1]").click()
driver.find_element_by_id("saveBtn").click()
time.sleep(1)
print('公告测试完毕')

######################################################课程文件##########################################################
# 上传课件
# 打开课程文件
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kj/wlkc_kjxxb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")

# 定位上传按钮，添加本地文件
print('测试课程文件')
js = "document.getElementById(\'fileupload\').style.display=\'block\'"
driver.execute_script(js)
driver.find_element_by_name("bt").send_keys("测试课件" + ticks)
driver.find_element_by_name("fileupload").send_keys("D:\listening.pdf")
print(driver.title)
time.sleep(5)
driver.find_element_by_id("sub").click()
print('文件完毕')

######################################################课程作业##########################################################
# 布置作业
print('测试课程作业')
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kczy/zy/teacher/bzzy?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
driver.find_element_by_name("bt").send_keys("测试全体作业" + ticks)
# 定位上传按钮，添加本地文件
js = "document.getElementById(\'fileupload\').style.display=\'block\'"
driver.execute_script(js)
driver.find_element_by_name("fileupload").send_keys("D:\listening.pdf")
time.sleep(5)
driver.find_element_by_name("jzsj").send_keys(tomorrow)
# driver.find_element_by_name("jzsj").send_keys("2019-04-15 10:00")
driver.find_element_by_id("goBtn").click()
print('作业测试完毕')

######################################################课程邮件##########################################################
# 打开课程邮件
print('测试课程邮件')
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/teacher/beforePageList?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# 新邮件
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
driver.find_element_by_class_name("ui-autocomplete-input").send_keys(
    "xiesp@tsinghua.edu.cn,chc@tsinghua.edu.cn,xdx2016@tsinghua.edu.cn,dj1005@tsinghua.edu.cn,zhongwenfeng@tsinghua.edu.cn")
driver.find_element_by_id("bt").send_keys("网络学堂自动测试:教师端系统正常" + ticks)
driver.find_element_by_id("submitButton").click()
print('邮件测试完毕')
##################################################退出网络学堂##########################################################
driver.find_element_by_xpath("//a[contains(text(),'退出登录')]").click()
driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[contains(text(),'确定')]").send_keys(
    Keys.ENTER)
time.sleep(2)
print('退出网络学堂')
driver.quit()
