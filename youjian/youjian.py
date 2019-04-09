#-*-coding:utf-8-*-

import smtplib,os
from email.mime.text import MIMEText
from email.header import Header

def fasongyoujian(filename):
    # 使用的是smtp服务器
    # 指定发送邮件的用户名
    send = "15712959187@163.com"
    # 指定接收邮件的邮箱
    recever = "1471375117@qq.com"
    # 指定邮件的主题
    title = u"优购移动端自动化测试报告"
    # 指定需要发送邮件的服务器
    emain_server = "smtp.163.com"
    # 指定发送邮件的用户名和密码
    username = "15712959187@163.com"
    password = "ylg123456"
    # 指定自动化测试报告的路径
    files1 = os.getcwd() + filename
    # 通过流将报告读取出来
    filename1 = open(files1, "rb")
    # 将流转为字符串
    emain_name = filename1.read()
    # 关闭流
    filename1.close()
    # 设置邮件的内容
    msg = MIMEText(emain_name, _subtype="html", _charset="UTF-8")
    # 设置主题
    msg['Subject'] = Header(title, "UTF-8")
    # 设置发送者和接受者
    msg['From'] = send
    msg['To'] = recever
    # 实例化smtp服务器
    smtp = smtplib.SMTP()
    # 开始连接服务器
    smtp.connect(emain_server)
    # 登陆服务器
    smtp.login(username, password)
    # 开始发送邮件
    smtp.sendmail(send, recever, msg.as_string())
    # 关闭服务器
    smtp.quit()

# fasongyoujian("/2019-04-09 14-08.html")


