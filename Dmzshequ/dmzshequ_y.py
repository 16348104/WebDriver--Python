import random
import time
import smtplib
from selenium import webdriver
from email.header import Header
from email.mime.text import MIMEText
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, TimeoutException, \
    ElementNotInteractableException

browser = webdriver.Firefox()
# browser = webdriver.Ie()
# browser = webdriver.Chrome()

# browser = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/wlxt/chromedriver')

# browser = webdriver.Safari()
browser.get('http://www.dmzshequ.com')
browser.maximize_window()
# browser.get('http://www.dmzshequ.com/plugin.php?id=dsu_paulsign:sign')#直接登录
browser.implicitly_wait(3)
print('登录Dmz社区!')
print(browser.title)
print('浏览器:' + browser.name)
time.sleep(1)
browser.find_element_by_xpath("//a[@class='deandengluanniu']").click()
time.sleep(1)


def login(user, password):
    browser.find_element_by_name("username").send_keys(user)
    browser.find_element_by_name("password").send_keys(password)


## 登录
login('zijing228', 'yu123456')
# login('milometer', 'ustb55')
browser.find_element_by_xpath('//button[@name="loginsubmit"]').click()
time.sleep(1)
print(browser.find_element_by_xpath('//*[@id="fwin_dialog"]//p').text)
browser.refresh()  # 刷新
time.sleep(3)
print("Dmz社区>", browser.find_element_by_xpath("//*[@id='pt']//a[2]").text)
try:
    browser.find_element_by_xpath("//ul[@class='qdsmile']//following-sibling::li")
    # except NoSuchElementException as msg:
except BaseException:
    print('今天已签到!')
    print(BaseException)
else:
    qdbq = len(browser.find_elements_by_xpath("//ul[@class='qdsmile']//following-sibling::li"))
    ran_bq = random.randrange(qdbq)
    xq = random.choice(['开心', '难过', '郁闷', '无聊', '发怒', '擦汗', '奋斗', '慵懒', '悲哀'])
    print('签到头像:', ran_bq)
    browser.find_elements_by_xpath("//ul[@class='qdsmile']//following-sibling::li").pop(ran_bq).click()
    browser.implicitly_wait(1)
    print('签到心情:', xq)
    browser.find_element_by_id('todaysay').send_keys('今天', xq, '!')
    time.sleep(3)
    browser.find_element_by_xpath("//*[@id='qiandao']/table[1]/tbody/tr/td/div/a").click()

##### 摇一摇
# try:
#     # 摇一摇按钮
#     browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a")
# except BaseException:
#     print(browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a").text)
#     print('今天摇过了!')
#     print(BaseException)
# else:
#     print(browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a").text)
#     browser.find_element_by_xpath("//*[@id='zzza_tixing']/div[1]/div[1]/a").click()
#     # browser.switch_to_alert()
#     time.sleep(5)
#     try:
#         print(browser.find_element_by_xpath("//*[@id='zzza_go']").text)
#         browser.find_element_by_xpath("//*[@id='zzza_go']").click()  # 摇金币
#         time.sleep(1)
#     # except UnexpectedAlertPresentException as msg_alert:
#     except BaseException:
#         print(BaseException)
#         print(browser.switch_to.alert.text)  # 如果签到不成功，接受摇金币时弹出alter
#         browser.switch_to.alert.accept()
#     else:
#         pass
#         # time.sleep(5)
#         # browser.find_element_by_xpath('//*[@id="yyl-random-box"]/div[1]').click()

browser.get('http://www.dmzshequ.com/plugin.php?id=yinxingfei_zzza:yinxingfei_zzza_hall')  ##每日摇摇乐链接
time.sleep(2)
print("Dmz社区>", browser.find_element_by_xpath("//*[@id='pt']//a[2]").text)
date = browser.find_element_by_xpath('//*[@class="zzza_hall_bottom_right_yjan_title"]//p').text
# if (date == 'zzza_hall_bottom_right_yjan_btn11'):
#     browser.find_element_by_xpath('//*[@id="nv_plugin"]/div[8]/div[3]/div[2]/div[3]/div[1]/div[1]/a').click()
#     print(browser.switch_to.alert.text)
#     browser.switch_to.alert.accept()
try:
    browser.find_element_by_xpath("//*[@id='zzza_go']")
except BaseException:
    print(date)
    print(NoSuchElementException)
else:
    # 摇金币
    browser.find_element_by_xpath("//*[@id='zzza_go']").click()  # 摇金币
    time.sleep(3)
    # 关闭对话框
    browser.find_element_by_xpath('//*[@id="yyl-random-box"]/div[1]').click()
time.sleep(5)
score = browser.find_element_by_xpath('//*[@id="nv_plugin"]/div[8]//ul/li[2]/span[2]').text
print('获得:', score)
print('今天任务已完成!')
current_time = time.strftime("%y-%m-%d %H:%M:%S", time.localtime(time.time()))
print('在', current_time, '退出Dmz社区')
browser.close()
##发邮件
print('去发邮件!')
smtpsever = 'smtp.126.com'
password = 'xdx2019'
user = 'xiaodaxing@126.com'
sender = 'xiaodaxing@126.com'
# receiver = 'pkucrjy2013@163.com'  # modify
# receiver = 'yumj@tsinghua.edu.cn'
receiver = '214423717@qq.com'
subject = 'Dmz' + ":" + score
mail_msg = '<html><h3>Hello,<br>Our task is done.</h3></html>'
# mail_msg = 'Hello,<br>Our task is done.'
msg = MIMEText(mail_msg, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = user
msg['To'] = receiver
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('Email has send out!')
time.sleep(1)
# browser.delete_all_cookies()
browser.quit()
