import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 发送邮件服务器
smtpsever = 'smtp.126.com'
# 用户名密码
# password = input("input:")
password = 'xdx2019'
user = 'xiaodaxing@126.com'
# 发件箱
sender = 'xiaodaxing@126.com'
# 收件箱
receiver = ['47283875@qq.com', 'wlxt@tsinghua.edu.cn']
# 邮件主题
subject = '阿里云监控截图'
# HTML类型邮件正文
msgRoot = MIMEText('<html><h3>Python Mail</h3></html>', 'html', 'utf-8')
# msgRoot = MIMEText('此为系统测试邮件，请勿直接回复！', 'plain', 'utf-8')
# mail_msg = 'Hello,Our task is done.'
sendfile = open('D:/Monitor.png', 'rb').read()
att = MIMEText(sendfile, 'png', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="Monitor.png"'
# msgRoot = MIMEText(mail_msg, 'html', 'utf-8')
msgRoot = MIMEMultipart('related')
msgRoot['Subject'] = subject
msgRoot['From'] = user
# msgRoot['To'] = receiver
# msg['To'] = receiver2
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
print('Success,Email has send out!')
