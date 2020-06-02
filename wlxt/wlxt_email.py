import os
import re
import time
import smtplib
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, \
    StaleElementReferenceException, ElementClickInterceptedException, ElementNotInteractableException
from selenium.webdriver.common.keys import Keys
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# driver = webdriver.Firefox()
driver = webdriver.Chrome()
# driver = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')  # mac  chrome
driver.delete_all_cookies()
time.sleep(1)


def time_format():
    current_time = time.strftime("%y-%m-%d %H-%M-%S", time.localtime(time.time()))
    return current_time


# 发邮件
def Send_mail():
    # 发送邮件服务器
    smtpsever = 'mail.tsinghua.edu.cn'
    # 用户名密码
    user = 'wlxt@tsinghua.edu.cn'
    password = 'wlxt88122'
    # 发件箱
    sender = 'xdx2016@tsinghua.edu.cn'
    # 收件箱
    receiver = ['wlxt@mail.tsinghua.edu.cn', 'yumj@tsinghua.edu.cn']
    # 邮件主题
    subject = '网络学堂课程文件监控报警'
    # 如名字所示Multipart就是分多个部分
    msgRoot = MIMEMultipart()
    msgRoot['Subject'] = subject
    msgRoot['From'] = user
    # ---这是文字部分---
    att = MIMEText("详见附件。" "此为系统测试邮件，请勿直接回复！", 'plain', 'utf-8')
    msgRoot.attach(att)
    # msgRoot = MIMEText('<html><h5>此为系统测试邮件，请勿直接回复！</h5></html>', 'html', 'utf-8')
    # msgRoot = MIMEText(mail_msg, 'html', 'utf-8')
    # ---这是附件部分---
    sendfile = open('C:/Users/zb/Downloads/FireShot/KJ.png', 'rb').read()  # modify
    att = MIMEText(sendfile, 'png', 'utf-8')
    att["Content-Type"] = 'application/octet-stream'
    att["Content-Disposition"] = 'attachment;filename="Monitor_KJ.png"'
    msgRoot.attach(att)
    try:
        smtp = smtplib.SMTP()
        smtp.set_debuglevel(1)
        smtp.connect(smtpsever, 25)
        smtp.login(user, password)
        smtp.sendmail(sender, receiver, msgRoot.as_string())
        smtp.quit()
        print('Success,Email has send out!')
    except smtplib.SMTPException as email:
        print('error', email)  # 打印错误


######################################################登录网络学堂######################################################
# 打开网络学堂
driver.get("http://learn.tsinghua.edu.cn")
driver.maximize_window()
print("======登录网络学堂=====")
print(driver.title)
print('测试浏览器:' + driver.name)
ticks = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
driver.find_element_by_name('i_user').send_keys('xdx2016')
driver.find_element_by_name('i_pass').send_keys('')
time.sleep(1)
driver.find_element_by_id("loginButtonId").click()
time.sleep(3)
print(driver.title, "第1个窗口")
driver.find_element_by_xpath("//a[contains(text(),'20740084-998')]").click()  # 正式20740084-998
time.sleep(1)
# 切换到第二个窗口
# 当前窗口句柄
window_1 = driver.current_window_handle
print('课程句柄:' + window_1)
windows = driver.window_handles  # 窗口总数
for current_window in windows:
    if current_window != window_1:
        driver.switch_to.window(current_window)
time.sleep(3)
print(driver.title, "第2个窗口")
print('新窗口句柄:' + current_window)
print('=====登录成功=====')
print("登录时间为:", ticks)
time.sleep(2)
#######################################################课程文件##########################################################
print('=====测试课程文件=====')
driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
time.sleep(2)
print('发课件')
driver.find_element_by_xpath(
    '//span[@class="rt right"]/child::a').click()  # 上课件
time.sleep(1)
# js = "document.getElementById('fileupload').style.display=\'block\'"
# driver.execute_script(js)
# 选课件类别
driver.find_element_by_xpath('//*[@id="kjfl-box"]/label[2]').click()
driver.find_element_by_name("bt").send_keys("测试课件" + ticks)
# 设置截止时间
# driver.find_element_by_xpath("//*[@id='endtime']").click()
# driver.find_element_by_xpath("//span[@class='laydate-btns-confirm']").click()
driver.find_element_by_name("fileupload").send_keys("D:\mov.mp4")  # modify
# driver.find_element_by_id('fileupload').send_keys(
#     r'/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/mov.mp4')  # mac上传文件
time.sleep(1)
driver.find_element_by_id("sub").click()
# time.sleep(2)
try:
    print('弹框结果:' + driver.find_element_by_css_selector(
        "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1"
    ).text)
except NoSuchElementException as msg:
    print('截图', msg)
    driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + 'KJ' + ".png")  # 截图modify
    time.sleep(1)
    Send_mail()
driver.find_element_by_xpath("//a[@id='wlxt_kj_wlkc_kjxxb']").click()
time.sleep(1)
print('预览课件')
str1 = driver.find_element_by_xpath("//tbody//tr[1]//td[8]//a[2]").get_attribute('class')
print(str1)
# 正则表达式
searchObj = re.search(r'disabled', str1, re.I)
if searchObj is None:
    print('文件类型可以预览!')
    # time.sleep(1)  # 等待预览
    driver.find_element_by_xpath("//tbody//tr[1]//td[8]//a[2]").click()  # 点预览按钮
    windows = driver.window_handles  # 显示所有句柄
    window_1 = driver.current_window_handle
    print('所有句柄:', windows)
    print("当前窗口：", window_1)
    # 切换窗口
    driver.switch_to.window(windows[2])  # 切换到第3个窗口
    time.sleep(1)
    try:
        driver.find_element_by_css_selector(
            "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1"
        )
    except NoSuchElementException:  # 课件正常转码
        print('课件已经转码！')
    # 课件转码中
    else:
        print(
            driver.find_element_by_css_selector(
                "body > div.zeromodal-container.alert > div.zeromodal-body > div.zeromodal-title1"
            ).text)
        driver.get_screenshot_as_file("C:/Users/zb/Downloads/FireShot/" + 'KJ' + ".png")  # 截图modify
        time.sleep(1)
        Send_mail()
    # Play Video
    try:
        driver.find_element_by_xpath(
            "//button[@class='vjs-big-play-button']").click()
        print('预览视频文件!')
        time.sleep(3)
    except NoSuchElementException as msg:
        print('暂无视频文件', msg)
    # 切换到第2个窗口
    driver.close()
    driver.switch_to.window(windows[1])
    print("当前窗口：", window_1)
else:
    print('文件不支持预览!', searchObj)
print('=====文件测试完毕=====')
time.sleep(2)
##################################################退出网络学堂###########################################################
# driver.find_element_by_xpath("//i[@class='webicon-out']").click()
# time.sleep(1)
# driver.find_element_by_xpath("//div[contains(@class,'zeromodal-footer')]//button[@class='btn btn-primary']").send_keys(
#     Keys.ENTER)
# print('=====退出网络学堂=====')
driver.delete_all_cookies()
time.sleep(1)
print('关闭浏览器，删除cookie')
driver.quit()
