print(str(ord('a'))) #以字符串形式输出a的Unicode码值
print(str(chr(9800))) #以字符串形式输出Unicode码9800的字符
print(chr(9800)) #输出Unicode码9800的字符
for i in range(12):
    print(str(chr(9800+i)))#输出Unicode码9800开始的12个字符，输出每一个字符后换行
for i in range(12):
    print(str(chr(9800+i)),end="|")#输出Unicode码9800开始的12个字符，输出每一个字符后增加一个“1”
                                    #并且不换行
