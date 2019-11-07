


import smtplib
# 发送字符串的邮件
from email.mime.text import MIMEText
# 处理多种形态的邮件主体我们需要 MIMEMultipart 类
from email.mime.multipart import MIMEMultipart
# 处理图片需要 MIMEImage 类   b396d7b686e6d9d9
from email.mime.image import MIMEImage

# 设置服务器所需信息
fromaddr = 'chercheren2008@sina.com'  # 邮件发送方邮箱地址
password = 'b396d7b686e6d9d9'  # 密码(部分邮箱为授权码)
toaddrs = ['xiesp@tsinghua.edu.cn', 'wlxt@tsinghua.edu.cn']  # 邮件接受方邮箱地址，注意需要[]包裹，这意味着你可以写多个邮件地址群发
# 设置email信息
# ---------------------------发送字符串的邮件-----------------------------
# 邮件内容设置
message = MIMEText('此为系统测试邮件，请勿直接回复！', 'plain', 'utf-8')
# 邮件主题
message['Subject'] = '教学评估测试完成!'
# 发送方信息
message['From'] = fromaddr
# 接受方信息可以不填
# message['To'] = toaddrs[0]
# message['To'] = toaddrs[1]
# ---------------------------------------------------------------------


# 登录并发送邮件
try:
    server = smtplib.SMTP('smtp.sina.cn')  # 新浪邮箱服务器地址，端口默认为25
    server.login(fromaddr, password)
    server.sendmail(fromaddr, toaddrs, message.as_string())
    print('Success,Email has send out!')
    server.quit()

except smtplib.SMTPException as e:
    print('error', e)  # 打印错误