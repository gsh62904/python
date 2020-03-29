#定义一个判断质数的函数
def iszhishu(m):#定义一个函数，判断输入值是否是质数
    flag = 1#定义一个标志用于存放是否是质数的状态（1是。2不是）
    for i in range(2,m):
        if m % i == 0:
            flag = 0
            break
    else:
        flag = 1
    return flag
#获得一个大于输入N的数字
n = int(eval(input())) #获取用户输入的一个整数数字
a = 0
out_str = ''
for a in range(0,n+1): #输出一个大于n的数
    if a <= n:
        a = a + 1
else:
    a = a
#获得5个大于输入N的质数    
counter0 = 5 #定义5次计数器
while counter0 > 0:
    if iszhishu(a) == 1:
        out_str += '{},'.format(str(a))
        counter0 = counter0 - 1#如果a是质数，计数器减一
    a = a + 1#在计数器次数内a循环增加，直到输出5个质数
print(out_str[:-1])
