usrName = input('请输入三到五十个之间的用户名')
name_len = len(usrName)  # len()函数可以检测字符长度
if name_len < 3:
    print('用户名至少三个字符')
elif name_len > 50:
    print('用户名不能多于五十个字符')
else:
    print('用户名有效')