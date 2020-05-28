import time
import smtplib
from selenium import webdriver
from email.header import Header
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from selenium.common.exceptions import NoSuchElementException, UnexpectedAlertPresentException, TimeoutException, \
    ElementNotInteractableException
# browser = webdriver.Firefox()
# browser = webdriver.Chrome()
browser = webdriver.Chrome(executable_path='/Users/xdx/PycharmProjects/WebDriver--Python/chromedriver')
browser.get('http://www.dmzshequ.com')
browser.maximize_window()
time.sleep(5)
##发邮件
print('去发邮件!')
smtpsever = 'mail.tsinghua.edu.cn'
user = '@tsinghua.edu.cn'
password = ''
sender = '@tsinghua.edu.cn'
receiver = ['yumj@tsinghua.edu.cn']
subject = 'DMZ摇一摇'
mail_msg = '<html><h3>Hello,<br>Our task is done.</h3></html>'
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
print('Email has send out!')
# browser.quit()