# 任意多个数字的乘积

def cmul(a,*b):
    ji = a
    for i in b:
       ji = ji * i
    return ji
print(eval("cmul({})".format(input('请输入数字用“,”分割'))))
