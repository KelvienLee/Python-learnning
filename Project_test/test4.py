import yagmail
args = {
    "user": "1154296130@qq.com",
    "password": "vjicrpvouiingeji",
    "host": "smtp.qq.com",
    "port": "465"
}

# 收件人列表
emailList = ["lixingqiang001@163.com"]

email = yagmail.SMTP(**args)
# 调用消息发送函数，参数分别是：to=收件人列表，subject 邮件标题，contents 邮件正文，cc 邮件抄送人
email.send(to=emailList, subject="邮件主题", contents="This is a test.")
