#货币转换
money=input()
if money[:3]=="RMB":
    dollor=(eval(money[3:]))/6.78
    print("USD{:.2f}".format(dollor))
else:
    renb=(eval(money[3:]))*6.78
    print("RMB{:.2f}".format(renb))
