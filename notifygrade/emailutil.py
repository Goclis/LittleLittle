# -*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText

def sendEmail(email_account, password, subject, content):
    msg = MIMEText(content, "plain", "utf-8")

    msg['Subject'] = subject
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
