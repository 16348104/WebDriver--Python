import smtplib
from email.header import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 发送邮件服务器
smtpsever = 'smtp.126.com'
# 用户名密码
# password = input("input:")
password = ''
user = 'xiaodaxing@126.com'
# 发件箱
sender = 'xiaodaxing@126.com'
# 收件箱
receiver = ['16348104@qq.com', 'wlxt@tsinghua.edu.cn']
# 邮件主题
subject = '阿里云监控截图'
# 如名字所示Multipart就是分多个部分
msgRoot = MIMEMultipart()
msgRoot['Subject'] = subject
msgRoot['From'] = user

# ---这是文字部分---
att = MIMEText("此为系统测试邮件，请勿直接回复！", 'plain', 'utf-8')
# msgRoot = MIMEText('<html><h3>Python Mail</h3></html>', 'html', 'utf-8')
# msgRoot = MIMEText(mail_msg, 'html', 'utf-8')
msgRoot.attach(att)

# ---这是附件部分---
sendfile = open('D:/Monitor.png', 'rb').read()
att = MIMEText(sendfile, 'png', 'utf-8')
att["Content-Type"] = 'application/octet-stream'
att["Content-Disposition"] = 'attachment;filename="Monitor.png"'
msgRoot.attach(att)
smtp = smtplib.SMTP()
smtp.set_debuglevel(1)
smtp.connect(smtpsever, 25)
smtp.login(user, password)
smtp.sendmail(sender, receiver, msgRoot.as_string())
smtp.quit()
print('Success,Email has send out!')
