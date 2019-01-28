import smtplib

from config import MAIL_SERVER, MAIL_PASSWORD, MAIL_PORT, MAIL_USERNAME


def send_result_to_email(email_to, url, result):
    smtp = smtplib.SMTP(MAIL_SERVER, MAIL_PORT)
    smtp.ehlo()
    smtp.starttls()
    smtp.login(MAIL_USERNAME, MAIL_PASSWORD)
    msg = str('"md5": "' + result + '"')
    msg = 'Subject: {}\n\n{}'.format('MD5 Hash of ' + url, msg)
    smtp.sendmail(MAIL_USERNAME, email_to, msg)
    smtp.quit()
