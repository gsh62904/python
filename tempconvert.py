#temp convert
temp = input("请输入温度，摄氏以C结尾，华氏以F结尾:")
if temp[-1]in ["C","c"]:
       f=eval(temp[0:-1])*1.8+32
       print("转换结果{:.2f}f".format(f))
elif temp[-1] in ["F","f"]:
       c=(eval(temp[0:-1])-32)/1.8
       print("转换结果{:.2f}c".format(c))
else:
       print("输入格式错误，请检查！")
       
       
   
