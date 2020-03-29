#请在...补充一行或多行代码
#CalStatisticsV1.py
def getNum():#获取用户不定长度的输入
    ls = []
    ch = '.[],'
    string = ''
    num = input()
    while num != '':
        ls.append(num)
        num = input()
    return ls
print(getNum())
