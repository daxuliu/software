import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr

from email import encoders


def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))


# password是你开启SMTP时给你的邮箱授权码
def send(from_addr, password, to_addr, smtp_server, msg_text, subject, title):
    msg = MIMEText(msg_text, 'plain', 'utf-8')
    msg['From'] = _format_addr(title + '<%s>' % from_addr)
    msg['To'] = _format_addr('管理员<%s>' % to_addr)
    msg['Subject'] = Header(subject, 'utf-8').encode()
    # 发送邮件
    server = smtplib.SMTP_SSL(smtp_server, 465)
    # 打印出和SMTP服务器交互的所有信息
    server.set_debuglevel(1)
    # 登录SMTP服务器
    server.login(from_addr, password)
    # sendmail():发送邮件，由于可以一次发给多个人，所以传入一个list邮件正文是一个str，as_string()把MIMEText对象变成str。
    server.sendmail(from_addr, to_addr, msg.as_string())
    print('邮件发送成功！')
    server.quit()


if __name__ == '__main__':
    from_addr = '1697935859@qq.com'
    password = 'yokhrbcxhllleceg'
    to_addr = ['2632546595@qq.com']
    smtp_server = 'smtp.qq.com'
    send(from_addr, password, to_addr, smtp_server, '这是一个email测试', '测试邮件', '测试email')