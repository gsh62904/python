#判断闰年
year , month = eval(input('请输入年月（格式为XXXX,X）：)'))
def runnian(year):#判断是否闰年
    if (year%4 == 0 and year%100 !=0) or year%400==0:
        flag = True
    else:
        flag = False
    return flag

def days(month):#判断月份
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [11,9,6,4]:
        days = 30
    else:
        if runnian(year)is True:
            days = 29
        else:
            days = 28
    return days
if runnian(year) is True:
    print('{}年是闰年，{}月有{}天。'.format(year,month,days(month)))
else :
    print('{}年不是闰年，{}月有{}天。'.format(year,month,days(month)))
    
