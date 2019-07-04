import smtplib
from email.header import Header
from email.mime.text import MIMEText

smtpsever = 'smtp.126.com'
# password = input("input:")
password = 'xdx2019'
user = 'xiaodaxing@126.com'
sender = 'xiaodaxing@126.com'
# receiver = ['yumj@tsinghua.edu.cn'], ['xdx2016@tsinghua.edu.cn']
# receiver = '16348104@qq.com'
receiver = 'pkucrjy2013@163.com'
# subject = 'Dmz'
subject = 'Network Connect'
# mail_msg = '<html><h3>Hello,<br>The network is connected.</h3></html>'
mail_msg = '<html><h3>Hello,<br>connected.</h3></html>'
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
