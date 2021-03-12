# -*- coding: UTF-8 -*-
# @Time:2021/3/12 11:39
# @Name:MailPost_SSL.py

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
import time

date = time.strftime("%Y-%m-%d",time.localtime())
receivers = [""]
sender = ""
mail_pass = ""
mail_subject = date +' '+ ""    # 邮件的标题
mail_context = ""          # 邮件内容
'''---------------------------------分割线------------------------------------'''
msg = MIMEMultipart()
msg["From"] = sender  # 发件人
msg["To"] = ";".join(receivers)  # 收件人
msg["Subject"] = mail_subject   # 邮件标题
# 邮件正文
msg.attach(MIMEText(mail_context, 'plain', 'utf-8'))
'''---------------------------------分割线------------------------------------'''
att1 = MIMEText(open("", "rb").read(), "base64", "utf-8")
# 文件地址
att1["Content-Type"] = "application/octet-stream"
# att1["Content-Disposition"] = 'attachment; filename="Testreporter-shebao.html"'-----英文附件写法
att1.add_header("Content-Disposition", "attachment", filename=("gbk", "", ""))
# 定义附件名称
msg.attach(att1)
'''---------------------------------分割线------------------------------------'''
att2 = MIMEText(open("", "rb").read(), "base64", "utf-8")
# 文件地址
att2["Content-Type"] = "application/octet-stream"
att2.add_header("Content-Disposition", "attachment", filename=("gbk", "", ""))
# 定义附件名称
msg.attach(att2)
'''---------------------------------分割线------------------------------------'''
try:
    # 启动SMTP服务ssl连接，端口465
    smtpObj = smtplib.SMTP_SSL('smtp.exmail.qq.com', 465)
    # 登陆账号
    smtpObj.login(sender,mail_pass)
    # 发送
    smtpObj.sendmail(sender, receivers, msg.as_string())
    print('Success: 邮件发送成功!')
    # 退出登录
    smtpObj.quit()
except smtplib.SMTPException:
    print('Error: 发送邮件失败!')