# coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import random

# driver = webdriver.Chrome(executable_path='C:/Users/zb/Desktop/test/python/chromedriver.exe')  # 定时任务
driver = webdriver.Chrome()
# driver = webdriver.Firefox()
# driver = webdriver.Ie()
# driver = webdriver.Firefox(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/geckodriver')  # mac firefox
# driver = webdriver.Chrome(executable_path='/Users/xiaodaxing/Downloads/PycharmProjects/wlxt/chromedriver')  # mac  chrome
# driver = webdriver.Safari() #Mac os
##################################################登录网络学堂###########################################################
print("======登录网络学堂=====")
print('测试浏览器:' + driver.name)
driver.get('http://learn.tsinghua.edu.cn')
driver.maximize_window()
driver.implicitly_wait(2)
print('登录后句柄:' + driver.current_window_handle)  # 登录网络学堂，【第一个窗口】
driver.find_element_by_name('i_user').clear()
driver.find_element_by_name('i_pass').clear()
# time.sleep(30)
driver.find_element_by_name('i_user').send_keys('')  # 键入用户名
driver.find_element_by_name('i_pass').send_keys('')  # 键入密码
driver.find_element_by_id('loginButtonId').send_keys(Keys.ENTER)
time.sleep(1)
# 进入课程【第二个窗口】
# driver.find_element_by_link_text('基于Linux的C++(20740084-998)').click()
driver.find_element_by_xpath("//a[contains(text(),'20740084-998')]").click()
print(driver.title)
# 【切换到第二个窗口】
window_1 = driver.current_window_handle  # 当前窗口句柄
print('课程句柄:' + window_1)
windows = driver.window_handles  # 窗口总数
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
print('新窗口句柄:')
print(current_window)
print('=====登录成功=====')

# ##################################################课程公告############################################################
print("=====测试课程公告=====")
driver.find_element_by_xpath("//a[@id='wlxt_kcgg_wlkc_ggb']").click()
time.sleep(3)  # 休眠
driver.find_element_by_xpath("//*[@id='table']/tbody/tr[1]/td[1]/a").click()
time.sleep(2)
ggfj = driver.find_element_by_xpath("//div[@id='ggfj']").is_displayed()
print(ggfj)
if ggfj:
    print('预览公告附件!')
    driver.find_element_by_xpath("//div[@id='ggfj']//a[@id='wjid']").click()  # 浏览公告附件
    # 【第3个窗口】
    windows = driver.window_handles  # 窗口总数
    print('所有句柄:')
    print(windows)
    driver.switch_to.window(windows[1])  # 切换到第2个窗口
    time.sleep(3)
else:
    print('无公告附件！')
    driver.find_element_by_id('backBtn').click()

print('=====公告测试完毕=====')

####################################################课程信息#############################################################
print('测试课程信息')
driver.find_element_by_css_selector('#wlxt_kc_v_kcxx_jskcxx').click()
time.sleep(3)
print('=======课程信息测试完毕=====')

####################################################课程文件#############################################################
print("=====测试课程文件=====")
driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
li = driver.find_elements_by_xpath("//i[contains(@class,'webicon-download downLoadFile')]")
ran = random.randint(1, 10) - 1  # 随机数
print('随机数:')
print(ran)
li.pop(ran).click()  # Download
print('下载课件')
driver.switch_to.frame('playFrame')
# print('预览课件')
# if driver.find_element_by_xpath("//img[@src='/res/app/wlxt/img/pbtn.png']").is_displayed():  # 文本文件
#     driver.find_element_by_xpath("//img[@src='/res/app/wlxt/img/pbtn.png']").click()
#     print('文本预览')
# elif driver.find_element_by_xpath("audio[@id='mp3']").is_displayed():  # 音频文件
#     driver.find_element_by_xpath("audio[@id='mp3']").click()
#     print("音频预览")
# elif driver.find_element_by_xpath("//button[@title='Play Video']//span[@class='vjs-control-text']").is_displayed():  # 视频文件
#     driver.find_element_by_xpath("//button[@title='Play Video']//span[@class='vjs-control-text']").click()
#     print("视频预览")
# else:
#     pass
driver.switch_to.parent_frame()
time.sleep(5)
print('=====课件测试完毕=====')

####################################################课程作业############################################################
print('=====测试课程作业=====')
driver.find_element_by_xpath("//a[@id='wlxt_kczy_zy']").click()
time.sleep(3)
driver.find_element_by_xpath('//*[@id="wtj"]/tbody/tr[1]/td[2]/a').click()
time.sleep(1)
driver.find_element_by_xpath('//input[@id="saveBtn"]').click()
driver.find_element_by_xpath('//textarea[@id="s_documention"]')
js = "document.getElementById('s_documention').value= new Date().toLocaleDateString()"
driver.execute_script(js)
driver.find_element_by_id('fileupload').send_keys(r'D:\listening.pdf')  # 上传文件
# driver.find_element_by_id('fileupload').send_keys(r'/Users/xiaodaxing/Desktop/1.jpg')  # Mac上传文件
driver.find_element_by_xpath("//input[@onclick='daijiao()']").click()
time.sleep(5)
print('=====作业测试完毕=====')

########################################################我的分组#########################################################
print('测试我的分组')
driver.find_element_by_css_selector('#wlxt_qz_v_wlkc_qzcyb').click()
time.sleep(3)
print('=====我的分组测试完毕=====')

####################################################课程邮件#############################################################
print('=====测试课程邮件=====')
driver.find_element_by_xpath("//a[@id='wlxt_mail_yj_yjxxb']").click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="list"]/tbody/tr[1]/td[2]/a').click()  # 浏览邮件
driver.find_element_by_id('returnButton').click()
driver.find_element_by_xpath('//span[@class="rt right"]/child::a').click()  # 去发邮件
addresses = driver.find_elements_by_xpath("//span[contains(@class,'text-icon')]")
for i in addresses:
    # if i.get_attribute('text') != '肖大兴':
    i.click()
    time.sleep(1)
driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys('wlxt@tsinghua.edu.cn')
driver.find_element_by_xpath('//ul[@id="myTags"]//li//input').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]/input').send_keys('xiesp@tsinghua.edu.cn')
driver.find_element_by_xpath('//ul[@id="myTags"]//li[2]//input').send_keys(Keys.ENTER)
time.sleep(1)
driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]/input').send_keys('dj1005@tsinghua.edu.cn')
driver.find_element_by_xpath('//ul[@id="myTags"]//li[3]//input').send_keys(Keys.ENTER)
time.sleep(1)
js = "document.getElementById('bt').value = new Date().toLocaleString();"
val = driver.execute_script(js)
driver.find_element_by_xpath('//input[@id="bt"]').send_keys('网络学堂自动化测试结果—学生端功能正常')
iframe = driver.find_element_by_xpath("//iframe[contains(@title,'nrStr')]")
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//body[starts-with(@class,'cke')]").send_keys('学生端功能正常')
driver.switch_to.default_content()
driver.find_element_by_xpath('//input[@id="submitButton"]').click()
time.sleep(3)
print('=====邮件测试完毕=====')

##################################################退出网络学堂############################################################
driver.find_element_by_xpath("//a[contains(text(),'退出登录')]").click()
time.sleep(2)
driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[contains(text(),'确定')]").send_keys(
    Keys.ENTER)
# js = "alert('12345')"
# driver.execute_script(js)
# driver.switch_to_alert().accept()
# driver.switch_to.alert.accept()
print('退出网络学堂')
driver.quit()
