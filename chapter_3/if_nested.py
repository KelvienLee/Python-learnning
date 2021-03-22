# 注意if else 函数判断起来具有顺序性，如果前面的条件满足了就不会执行后面的函数，在书写时注意逻辑性

has_house = True
has_car = False
low_level = 0
if not low_level:
    if has_house and has_car:
        print('you are very good!')
    elif has_house or has_car:
        print('you are good!')
    else:
        print('ok ok!')
else:
    print('你不符合要求')