import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

user = "chercheren2008@sina.com"
pwd = ""
to = ["16348104@qq.com", ]

# 如名字所示Multipart就是分多个部分b396d7b686e6d9d9
msg = MIMEMultipart()
msg["Subject"] = "don't panic"
msg["From"] = user
msg["To"] = to

# ---这是文字部分---
part = MIMEText("此为系统测试邮件，请勿直接回复！", 'plain', 'utf-8')
msg.attach(part)

# ---这是附件部分---
# xlsx类型附件
# part = MIMEApplication(open('foo.xlsx', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.xlsx")
# msg.attach(part)

# jpg/png类型附件
part = MIMEApplication(open('D:/Monitor.png', 'rb').read())
part.add_header('Content-Disposition', 'attachment', filename="Monitor.png")
msg.attach(part)

# pdf类型附件
# part = MIMEApplication(open('foo.pdf', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.pdf")
# msg.attach(part)

# mp3类型附件
# part = MIMEApplication(open('foo.mp3', 'rb').read())
# part.add_header('Content-Disposition', 'attachment', filename="foo.mp3")
# msg.attach(part)

# 登录并发送邮件
try:
    server = smtplib.SMTP("smtp.sina.cn", timeout=30)  # 连接smtp邮件服务器,端口默认是25
    server.set_debuglevel(1)
    # server.connect(server,25)
    server.login(user, pwd)  # 登录服务器
    server.sendmail(user, to, msg.as_string())  # 发送邮件
    print('Success,Email has send out!')
    server.quit()
except smtplib.SMTPException as e:
    print('error', e)  # 打印错误
