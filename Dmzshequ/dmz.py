import time
import smtplib
from selenium import webdriver
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, TimeoutException, \
    ElementNotInteractableException

# browser = webdriver.Firefox(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/geckodriver')
browser = webdriver.Firefox()
# browser = webdriver.Chrome()
browser.get('http://www.dmzshequ.com')
browser.maximize_window()
time.sleep(2)
print(browser.title)
# js_login = "showWindow('login', this.href)"
# browser.execute_script(js_login)
browser.find_element_by_xpath("//div[@class='deandl_before']/a[1]").click()
time.sleep(3)


def login(user, password):
    browser.find_element_by_name("username").send_keys(user)
    browser.find_element_by_name("password").send_keys(password)


## 登录
login('', '')
time.sleep(2)
browser.find_element_by_name('seccodeverify').send_keys()

# 发邮件
print('去发邮件!')
smtpsever = 'smtp.sina.com'
user = 'chercheren2008@sina.com'
password = ''
sender = 'chercheren2008@sina.com'
receiver = ['yumj@tsinghua.edu.cn', '214423717@qq.com']
subject = 'DMZ摇一摇'
mail_msg = '<html><h3>Successfully！<br>Our task is done.</h3></html>'
msg = MIMEText(mail_msg, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = user
# msg['To'] = receiver
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('Successfully！Email has send out!')
