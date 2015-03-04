#!/usr/bin/env python
# -*- coding:utf-8 -*-

import threading
import commands
import time
import sys
import smtplib
from email.mime.text import MIMEText


# 邮箱的账户密码
username = 'username'
password = 'password'
latest_ip = ''


# 给邮箱本身发送一封邮件
# 发送成功返回Ture，失败返回False
def send_email(email_account, password, content):
	msg = MIMEText(content)

	msg['Subject'] = 'Your Latest IP'
	msg['From'] = email_account
	msg['To'] = email_account

	try:
		session = smtplib.SMTP('mail.seu.edu.cn')
		session.ehlo()
		session.starttls()
		session.ehlo()
		session.login(email_account, password)

		session.sendmail(email_account, [email_account], msg.as_string())
		session.quit()

		return True
	except:
		return False


# 获取eth0的IP，硬编码
def get_eth0_ip():
	ifconfig_info = commands.getoutput('ifconfig')
	lines = [s.strip() for s in ifconfig_info.split('\n')]
	inet_addr = [s.strip() for s in lines[1].split('  ')][0]
	return inet_addr[len('inet addr:') :]


# Python setInterval
def set_interval(func, sec):
    def func_wrapper():
        set_interval(func, sec)
        func()
    t = threading.Timer(sec, func_wrapper)
    t.start()
    return t


# 定期的检查IP，当发现变化时，发送邮件进行通知
# 邮件不一定能发送成功，当成功时才修改IP，以方便下次检查时重新尝试发送邮件,
# 这样能够尽量保证通过邮件发送出去的IP是正确的学校内网IP
def check():
    global latest_ip

    new_ip = get_eth0_ip()
    if latest_ip != new_ip:
        if send_email(username, password, new_ip):
            latest_ip = new_ip


# 验证账号密码
def verify(un, pw):
	try:
		session = smtplib.SMTP('mail.seu.edu.cn')
		session.ehlo()
		session.starttls()
		session.ehlo()
		session.login(un, pw)
		session.quit()

		return True
	except:
		return False


# 对账户密码进行验证，验证通过后发送一次IP邮件后启动定时器
def main():
	if verify(username, password):
		global latest_ip

		# 刚启动的时候发送一次，以防重启导致的IP变化
		latest_ip = get_eth0_ip()
		send_email(username, password, latest_ip)
		
		set_interval(check, 5)
	else:
		print u'存在错误，请尝试重新输入账号密码'


if __name__ == '__main__':
	main()

