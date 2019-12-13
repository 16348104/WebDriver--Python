import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpsever = 'smtp.126.com'
# password = input("input:")
password = ''
user = ''
sender = ''
# receiver = ['yumj@tsinghua.edu.cn', 'xdx2016@tsinghua.edu.cn']
receiver = '16348104@qq.com'
# receiver0 = 'xdx2016@tsinghua.edu.cn'
# subject = 'Dmz'
subject = 'Network Connect'
mail_msg = '<html><h3>Hello,<br>The network is connected.</h3></html>'
# mail_msg = 'Hello,Our task is done.'
msg = MIMEText(mail_msg, 'html', 'utf-8')
msg['Subject'] = Header(subject, 'utf-8')
msg['From'] = user
msg['To'] = receiver
# msg['To'] = receiver2
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msg.as_string())
smtp.quit()
print('Email has send out!')
