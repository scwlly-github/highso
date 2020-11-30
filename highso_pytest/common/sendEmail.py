#!/usr/bin/python3
# coding=utf-8
import time,os,smtplib,unittest
from highso_pytest.common.myLog import MyLog
from highso_pytest.config.readConfig import ReadConfig
from highso_pytest.common.HTMLTestRunnerNew import HTMLTestRunner
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

local_readConfig = ReadConfig()
#取最新测试报告
def new_file(test_dir):
    # 列举test_dir目录下的所有文件，结果以列表形式返回。
    lists = os.listdir(test_dir)
    # sort按key的关键字进行排序，lambda的入参fn为lists列表的元素，获取文件的最后修改时间
    # 最后对lists元素，按文件修改时间大小从小到大排序。
    lists.sort(key=lambda fn: os.path.getmtime(test_dir  + fn))
    # 获取最新文件的绝对路径
    file_path = os.path.join(test_dir, lists[-1])
    return file_path

#发送邮件，发送最新测试报告html
def send_email(newfile):
    # 打开文件
    f = open(newfile, 'rb')
    # 读取文件内容
    mail_body = f.read()
    # 关闭文件
    f.close()
    logger = MyLog()
    host = local_readConfig.get_email('mail_host')  # 邮箱服务器
    # 要在163有限设置授权码（即客户端的密码），否则会报535
    user = local_readConfig.get_email('mail_user')  # 发件人用户名
    password = local_readConfig.get_email('mail_pass')  # 发件人邮箱授权码，非登录密码
    sender = local_readConfig.get_email('sender')  # 发件人邮箱
    title = local_readConfig.get_email('title')  # 邮件标题
    # 多个接收邮箱，单个收件人的话，直接是receiver='XXX@126.com'
    receive_user = ['shixf@tydic.com','834950026@qq.com']
    msg = MIMEMultipart('mixed')
    msg_html1 = MIMEText(mail_body, 'html', 'utf-8')
    msg.attach(msg_html1)

    msg_html = MIMEText(mail_body, 'html', 'utf-8')
    msg_html["Content-Disposition"] = 'attachment; filename="TestReport.html"'
    msg.attach(msg_html)
    # 要加上msg['From']这句话，否则会报554的错误。
    msg['From'] = "{}".format(sender)  # 发件人
    # 多个收件人
    msg['To'] = ",".join(receive_user)  # 收件人
    msg['Subject'] = Header(title, 'utf-8')
    try:
        # 连接发送邮件
        smtp = smtplib.SMTP_SSL(host,465)
        #smtp.connect(smtpserver, 25)
        smtp.login(user, password)
        smtp.sendmail(sender, receive_user, msg.as_string())
        smtp.quit()
        logger.info("邮件发送成功！")
    except smtplib.SMTPException as e:
        logger.error("邮件发送失败！请检查邮件配置%s" % e)

if __name__ == '__main__':
    # 指定测试用例为当前文件夹下的test_case目录
    test_dir = r'/Users/scwlly/Desktop/automated_test/highso/highso_pytest/testcase'
    # 测试报告的路径
    test_report_dir = r'/Users/scwlly/Desktop/automated_test/highso/highso_pytest/test_reporter'
    discover = unittest.defaultTestLoader.discover(test_dir,'test_tv_show.py')
    now = time.strftime('%Y-%m-%d_%H:%M:%S_')
    filename = test_report_dir + now + 'report.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp, title=u'Douban Test',
                            description=u'用例执行情况：')
    runner.run(discover)
    fp.close()
    # 取最新测试报告
    new_report = new_file(test_report_dir)
    # 发送邮件，发送最新测试报告html
    send_email(new_report)
