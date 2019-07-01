import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpsever = 'smtp.126.com'
password = 'xdx2019'
user = 'xiaodaxing@126.com'
sender = 'xiaodaxing@126.com'
receiver1 = 'yumj@tsinghua.edu.cn'
receiver2 = 'xiaodaxing@126.com'
subject = 'Dmz'
msg = MIMEText('<html><h3>Hello,<br>Our task is done.</h3></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = user
msg['To'] = receiver1
msg['To'] = receiver2
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver1, msg.as_string())
smtp.sendmail(sender, receiver2, msg.as_string())
smtp.quit()
print('email has send out!')
