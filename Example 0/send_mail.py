import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpsever = 'smtp.sina.cn'
password = '2008@sina'
user = 'dxx2018@sina.cn'
sender = 'dxx2018@sina.cn'
receiver = 'xdx2016@mail.tsinghua.edu.cn'
subject = 'Python email test'
msg = MIMEText('<html><h2>Hello</h2></html>', 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = user
msg['To'] = receiver
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('email has send out!')
