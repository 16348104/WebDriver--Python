import time
import smtplib
from selenium import webdriver
from email.header import Header
from email.mime.text import MIMEText
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, TimeoutException, \
    ElementNotInteractableException
browser = webdriver.Firefox()
# browser = webdriver.Chrome()
browser.get('http://www.dmzshequ.com')
browser.maximize_window()
time.sleep(5)
##发邮件
print('去发邮件!')
smtpsever = 'mail.tsinghua.edu.cn'
password = ''
user = 'xdx2016@tsinghua.edu.cn'
sender = 'XiaoDaXing2019'
receiver =[ 'yumj@tsinghua.edu.cn']
mail_msg = '<html><h3>Hello,<br>Our task is done.</h3></html>'
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