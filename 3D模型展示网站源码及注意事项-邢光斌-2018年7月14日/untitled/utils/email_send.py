# _*_ coding: utf-8 _*_
__auther__ = '刘凌晨'
__date__ = '2018/3/28 16:32'

from random import Random
# 导入Django自带的邮件模块
from django.core.mail import send_mail

from book.models import EmailVerifyRecord
from untitled.settings import EMAIL_FROM


#生成随机字符串
def readom_str(random_length=8):
    str = ""
    #表示随机生成的字符串必须在这些里面进行选取
    chars = 'AaBbCcDdEeFfGgHhIiJjKkLlMmNnOoPpQqRrSsTtUuVvWwXxYyZz0123456789'
    length = len(chars) - 1;
    random = Random()
    for i in range(random_length):
        str += chars[random.randint(0,length)]
    return str

#发送注册邮件
def send_register_email(email,send_type="register"):
    email_record = EmailVerifyRecord();
    if send_type == "send_type":
        code = readom_str(4)
    else:
        code = readom_str(16)
    #将随机生成的code放入链接
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type

    email_record.save()

    #定义邮件内容
    email_title = ""
    email_body = ""

    if send_type == "register":
        email_title = "慕课在线网注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        # 使用Django内置函数完成邮件发送。四个参数：主题，邮件内容，从哪里发，接受者list
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "forget":
        email_title = "慕课在线网注册密码重置链接"
        email_body = "请点击下面的链接重置你的密码：http://127.0.0.1:8000/reset/{0}".format(code)
        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass
    elif send_type == "update_email":
        email_title = "慕课在线邮箱修改验证码"
        email_body = "你的邮箱验证码为:{0}".format(code)

        send_status = send_mail(email_title, email_body, EMAIL_FROM, [email])
        if send_status:
            pass