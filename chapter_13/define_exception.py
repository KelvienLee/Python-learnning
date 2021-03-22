# 自定义异常类

class ValidateError(ValueError):
    def __init__(self, message, *args, **kwargs):
        super().__init__(message, *args, **kwargs)


def validate_accout(username, password):
    if username == '':
        raise ValidateError('用户名不能为空')
    if password == '':
        raise ValidateError('密码不能为空')
    if username != 'kelvin' or password != '123456':
        raise ValidateError('用户名和密码不匹配')


username = input('请输入用户名：')
password = input('请输入密码：')
try:
    validate_accout(username, password)
except ValueError as va:
    print(va)
else:
    print('用户名和密码正确')




























