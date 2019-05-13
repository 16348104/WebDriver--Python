# coding=utf-8
from selenium import webdriver
import time

from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys

# driver = webdriver.Chrome(executable_path='C:/Users/zb/Desktop/test/python/chromedriver.exe')  # modify
# driver = webdriver.Firefox()
driver = webdriver.Chrome()


# driver = webdriver.Firefox(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os

def time_format():
    current_time = time.strftime('%Y%m%d%H%M%S', time.localtime(time.time()))
    return current_time


######################################################登录网络学堂######################################################
# 打开网络学堂
driver.get("http://learn.tsinghua.edu.cn")
driver.maximize_window()
print("======登录网络学堂=====")
print(driver.title)
print('测试浏览器:' + driver.name)
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
# 计算明天时间
tomorrow = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time() + 3600))
print("当前时间戳为:", ticks)
# print ("当前时间戳为:", tomorrow)

driver.find_element_by_name("i_user").send_keys("")
driver.find_element_by_name("i_pass").send_keys("")
driver.find_element_by_id("loginButtonId").click()
time.sleep(1)
######################################################课程公告##########################################################
# print('测试课程公告')
# driver.get("http://learn.tsinghua.edu.cn/f/wlxt/kcgg/wlkc_ggb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# # driver.find_element_by_xpath("//dd[1]//div[1]//div[1]//a[1]").click()
# # 发布公告
# time.sleep(2)
# driver.find_element_by_name("bt").send_keys("测试公告" + ticks)
# driver.find_element_by_xpath("//div[@class='list title notext']//label[1]").click()
# driver.find_element_by_xpath("//div[@class='list order clearfix']//label[1]").click()
# time.sleep(1)
# driver.find_element_by_id("saveBtn").click()
# print('公告测试完毕')
# time.sleep(3)
######################################################课程文件##########################################################
# # 打开课程文件
# driver.get("http://learn.tsinghua.edu.cn/f/wlxt/kj/wlkc_kjxxb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# # driver.find_element_by_xpath("//dd[1]//div[1]//div[1]//a[4]").click()  # 上传课件
# # 定位上传按钮，添加本地文件
# print('测试课程文件')
# js = "document.getElementById('fileupload').style.display=\'block\'"
# driver.execute_script(js)
# driver.find_element_by_name("bt").send_keys("测试课件" + ticks)
# driver.find_element_by_name("fileupload").send_keys("D:\listening.pdf")  # modify
# time.sleep(5)
# driver.find_element_by_id("sub").click()
# print('文件完毕')
# time.sleep(3)
######################################################课程作业##########################################################
# 布置作业
print('测试课程作业')
driver.get(
    "http://learn.tsinghua.edu.cn/f/wlxt/kczy/zy/teacher/bzzy?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# driver.find_element_by_xpath("//dd[1]//div[1]//div[1]//a[3]").click()
driver.find_element_by_name("bt").send_keys("测试全体作业" + ticks)
# 定位上传按钮，添加本地文件
js = "document.getElementById('fileupload').style.display=\'block\'"
driver.execute_script(js)
driver.find_element_by_name("fileupload").send_keys("D:/listening.pdf")  # modify
time.sleep(5)
# 设置截止时间
# driver.find_element_by_name("jzsj").send_keys(tomorrow)
scroll = "document.documentElement.scrollTop = 10000;"
driver.execute_script(scroll)
time.sleep(1)
driver.find_element_by_id('endtime').click()
time.sleep(2)
try:
    driver.find_element_by_xpath("//span[@class='laydate-btns-confirm']")
except NoSuchElementException as msg:
    print(msg)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/" + time_format() + ".png")
else:
    time.sleep(1)
    driver.find_element_by_xpath("//span[@class='laydate-btns-confirm']").click()

driver.find_element_by_id("goBtn").click()
time.sleep(5)
print('作业测试完毕')
######################################################课程邮件##########################################################
# 打开课程邮件
# print('测试课程邮件')
# driver.get("http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/teacher/beforePageList?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
#
# # 新邮件
# # driver.get("http://learn.tsinghua.edu.cn/f/wlxt/mail/yj_yjxxb/teacher/beforeAdd?wlkcid=2018-2019-226ef84e7689589e901689906e324686a")
# driver.find_element_by_xpath("//a[contains(text(),'新邮件')]").click()
# driver.find_element_by_class_name("ui-autocomplete-input").send_keys(
#     "xiesp@tsinghua.edu.cn,chc@tsinghua.edu.cn,xdx2016@tsinghua.edu.cn,dj1005@tsinghua.edu.cn,zhongwenfeng@tsinghua.edu.cn")
# driver.find_element_by_id("bt").send_keys("网络学堂自动测试:教师端系统正常" + ticks)
# driver.find_element_by_id("submitButton").click()
# print('邮件测试完毕')
# time.sleep(3)
##################################################退出网络学堂##########################################################
# driver.find_element_by_xpath("//a[contains(text(),'退出登录')]").click()
# driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[contains(text(),'确定')]").send_keys(
#     Keys.ENTER)
# time.sleep(2)
# print('退出网络学堂')
# driver.quit()
