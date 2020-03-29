#将输入的数字转换成汉字数字
chn = "零一二三四五六七八九"
num = input()
a = ''
for i in num:
    a = a + chn[eval(i)]
print("{0:^30}".format(a))
