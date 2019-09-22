import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 发送邮件服务器
smtpsever = 'smtp.126.com'
# 用户名密码
# password = input("input:")
password = 'xdx2016'
user = 'xiaodaxing@126.com'
# 发件箱
sender = 'xiaodaxing@126.com'
# 收件箱
# receiver = ['yumj@tsinghua.edu.cn'], ['xdx2016@tsinghua.edu.cn']
receiver = '16348104@qq.com'
# receiver0 = 'xdx2016@tsinghua.edu.cn'
# 邮件主题
subject = 'Python Mail'
# HTML类型邮件正文
msgRoot = MIMEText('<html><h3>Hello</h3></html>', 'html', 'utf-8')
# mail_msg = 'Hello,Our task is done.'
sendfile = open('D:/Homework.pdf', 'rb').read()
att = MIMEText(sendfile, 'pdf', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="Homework.pdf"'
# msgRoot = MIMEText(mail_msg, 'html', 'utf-8')
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = user
msgRoot['To'] = receiver
# msg['To'] = receiver2
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
print('success!')
